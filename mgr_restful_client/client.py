#   Copyright 2013 David Moreau Simard
#   Copyright 2019 Changcheng Liu
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#   Author: Changcheng Liu <changcheng.liu@aliyun.com>
#           David Moreau Simard <moi@dmsimard.com>
#

"""
A ceph-mgr/RESTful plugin interface that handles RESTful calls and responses.
"""

import logging
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import subprocess
from collections import defaultdict

try:
    import json
except ImportError:
    import simplejson as json

import client-mgr-restful.exceptions as exceptions

class respdict(defaultdict):
    def __init__(self):
        super(respdict, self).__init__(respdict)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

class RestfulClient(object):

    def __init__(self, **params):
        """
        Initialize the class, get the necessary parameters
        """
        self.user_agent = 'client-mgr-restful'

        self.params = params
        self.log = self.log_wrapper()

        self.log.debug("Params: {0}".format(str(self.params)))

        if 'endpoint' in self.params:
            self.endpoint = self.params['endpoint']
        else:
            # default endpoint
            self.endpoint = 'https://localhost:8003/'

        if 'timeout' not in self.params:
            self.timeout = None

        self.http = requests.Session()

    def _restful_check_active(self):
        rst = subprocess.Popen("curl --connect-timeout 5 -k https://localhost:8003/ 2>&1", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return rst.wait()

    def _get_admin_key(self):
        if self._restful_check_active() != 0:
            raise Exception('RESTful plugin is not active. Please restart')
        p = subprocess.Popen("ceph restful list-keys --connect-timeout 5", shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        if p.wait() != 0:
            raise Exception('RESTful plugin: can not get list-keys. Please restart')
        rst = p.stdout.read()
        rst = json.loads(rst)
        if 'admin' not in rst.keys():
            raise Exception('admin user and its password not exist in RESTful plugin')
        admin_key = str(rst['admin'])
        return ("admin", admin_key)

    def _request(self, url, method, **kwargs):
        if self.timeout is not None:
            kwargs.setdefault('timeout', self.timeout)

        kwargs.setdefault('headers', kwargs.get('headers', {}))
        kwargs['headers']['User-Agent'] = self.user_agent

        try:
            if kwargs['body'] is 'json':
                kwargs['json']['format'] = 'json'
            elif kwargs['body'] is 'text':
                kwargs['json']['format'] = 'plain'
            else:
                raise exceptions.UnsupportedRequestType()
        except KeyError:
            # Default if body type is unspecified is text/plain
            kwargs['json']['format'] = 'json'

        # Optionally verify if requested body type is supported
        try:
            if kwargs['body'] not in kwargs['supported_body_types']:
                raise exceptions.UnsupportedBodyType()
            else:
                del kwargs['supported_body_types']
        except KeyError:
            pass

        try:
            del kwargs['body']
        except KeyError:
            pass

        self.log.debug("{0} URL: {1}{2} - {3}"
                       .format(method, self.endpoint, url, str(kwargs)))

        resp = self.http.request(method, self.endpoint + url, auth = self._get_admin_key(), verify = False, **kwargs)
        rst = json.loads(resp.text)
        ret_resp = respdict()
        ret_resp.status_code = resp.status_code
        ret_resp.ok = True

        if rst['has_failed'] == True or rst['state'] != 'success' or len(rst['failed']) != 0 or rst['is_finished'] != True:
            ret_resp.ok = False
            ret_resp.reason = rst['failed'][0]['outs']
            ret_resp.status_code = requests.codes.ok + 1
            body = None
            return ret_resp, body

        try:
            finished = rst['finished'][0]
            body = {}
            if (len(finished) == 0):
                body[u'status'] = u'ko'
                ret_resp.ok = False
            elif kwargs['json']['format'] is 'json':
                body[u'status'] = u'ok'
                body[u'output'] = json.loads(str(finished['outb'].strip('\n')))
            else:
                #do not add strip here unless you know what you are doing
                body = finished['outb']
        except ValueError:
            body = None

        return ret_resp, body

    def get(self, url, **kwargs):
        return self._request(url, 'GET', **kwargs)

    def post(self, url, **kwargs):
        return self._request(url, 'POST', **kwargs)

    def put(self, url, **kwargs):
        return self._request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        return self._request(url, 'DELETE', **kwargs)

    def log_wrapper(self):
        """
        Wrapper to set logging parameters for output
        """
        log = logging.getLogger('client.py')

        # Set the log format and log level
        try:
            debug = self.params["debug"]
            log.setLevel(logging.DEBUG)
        except KeyError:
            log.setLevel(logging.INFO)

        # Set the log format.
        stream = logging.StreamHandler()
        logformat = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%b %d %H:%M:%S')
        stream.setFormatter(logformat)

        log.addHandler(stream)
        return log
