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
#   Authors: David Moreau Simard <moi@dmsimard.com>
#            Changcheng Liu <changcheng.liu@aliyun.com>
#

import mgr_restful_client.client as client
import mgr_restful_client.exceptions as exceptions
import json


class CephWrapper(client.RestfulClient):
    def __init__(self, **params):
        super(CephWrapper, self).__init__(**params)
        self.user_agent = 'client-mgr-restful-wrapper'

    ###
    # root GET calls
    ###
    def df(self, detail=None, **kwargs):
        if detail is not None:
            return self.post('request?wait=1', json = {'prefix': 'df', 'detail': detail}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'df'}, **kwargs)

    def fsid(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'fsid'}, **kwargs)

    def health(self, detail=None, **kwargs):
        if detail is not None:
            return self.post('request?wait=1', json = {'prefix': 'health', 'detail': detail}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'health'}, **kwargs)

    def quorum_status(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'quorum_status'}, **kwargs)

    def report(self, tags=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def status(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'status'}, **kwargs)

    ###
    # root PUT calls
    ###
    def compact(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def heap(self, heapcmd, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def injectargs(self, injected_args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def log(self, logtext, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def quorum(self, quorumcmd, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def scrub(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def tell(self, target, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # auth GET calls
    ###
    def auth_export(self, entity=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_get(self, entity, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_get_key(self, entity, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_list(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_print_key(self, entity, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # auth PUT calls
    ###
    def auth_add(self, entity, caps={}, file=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_caps(self, entity, caps={}, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_del(self, entity, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'auth del', 'entity': entity}, **kwargs)

    def auth_get_or_create(self, entity, caps={}, **kwargs):
        full_caps = list()
        if caps:
            for key in caps:
                permissions = caps[key]
                full_caps.append('{0} {1}'.format(key, permissions))
            return self.post('request?wait=1', json = {'prefix': 'auth get-or-create', 'entity': entity, 'caps': full_caps}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'auth get-or-create', 'entity': entity}, **kwargs)

    def auth_get_or_create_key(self, entity, caps={}, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def auth_import(self, file):
        # XXX-TODO: Implement file input
        raise exceptions.FunctionNotImplemented()

    ###
    # config-key GET calls
    ###
    def config_key_exists(self, key, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def config_key_get(self, key, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def config_key_list(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # mds GET calls
    ###
    def mds_compat_show(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_dump(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_getmap(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_stat(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # mds PUT calls
    ###
    def mds_add_data_pool(self, pool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_cluster_down(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_cluster_up(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_compat_rm_compat(self, feature, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_compat_rm_incompat(self, feature, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_deactivate(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_fail(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_newfs(self, metadata, data, sure, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_remove_data_pool(self, pool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_rm(self, gid, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_rmfailed(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_set_allow_new_snaps(self, sure, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_set_max_mds(self, maxmds, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_setmap(self, epoch, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_stop(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_tell(self, who, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mds_unset_allow_new_snaps(self, sure, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # mon GET calls
    ###
    def mon_dump(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.post('request?wait=1', json = {'prefix': 'mon dump', 'epoch': epoch}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'mon dump'}, **kwargs)

    def mon_getmap(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mon_stat(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mon_status(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # mon PUT calls
    ###
    def mon_add(self, name, addr, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def mon_remove(self, name, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # osd GET calls
    ###
    def osd_blacklist_ls(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_dump(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_rule_dump(self, name=None, **kwargs):
        if name is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd crush rule dump', 'name': name}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd crush rule dump'}, **kwargs)

    def osd_crush_rule_list(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_rule_ls(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd crush rule ls'}, **kwargs)

    def osd_crush_tree(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd crush tree'}, **kwargs)

    def osd_df(self, output_method = None, **kwargs):
        if output_method is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd df', 'output_method': output_method}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd df'}, **kwargs)

    def osd_dump(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_find(self, id, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_getcrushmap(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_getmap(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_getmaxosd(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_ls(self, epoch=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_lspools(self, auid=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_map(self, pool, object, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_perf(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_get_pool_param(self, pool, var, **kwargs):
        return self.osd_pool_get(pool, var, **kwargs)

    def osd_pool_get(self, pool, var, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd pool get', 'pool': pool, 'var': var}, **kwargs)

    def osd_pool_stats(self, name=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_get_pool_quota(self, pool, **kwargs):
        return self.osd_pool_get_quota(pool, **kwargs)

    def osd_pool_get_quota(self, pool, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd pool get-quota', 'pool': pool}, **kwargs)

    def osd_pool_ls(self, detail=None, **kwargs):
        if detail is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd pool ls', 'detail': detail}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd pool ls'}, **kwargs)

    def osd_stat(self, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd stat'}, **kwargs)

    def osd_tree(self, epoch=None, **kwargs):
        if epoch is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd tree', 'epoch': epoch}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd tree'}, **kwargs)

    ###
    # osd PUT calls
    ###
    def osd_blacklist(self, blacklistop, addr, expire, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_create(self, uuid=None, id=None, **kwargs):
        jsont = dict()
        jsont['prefix'] = 'osd create'
        if uuid is not None:
            jsont['uuid'] = uuid
        if id is not None:
            jsont['id'] = id
        return self.post('request?wait=1', json = jsont, **kwargs)

    def osd_crush_add(self, id, weight, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_add_bucket(self, name, type, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd crush add-bucket', 'name': name, 'type': type}, **kwargs)

    def osd_crush_create_or_move(self, id, weight, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_link(self, name, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_move(self, name, args, **kwargs):
        #support only one arg e.g. "A=B"
        full_caps = list()
        full_caps.append(args)
        return self.post('request?wait=1', json = {'prefix': 'osd crush move', 'name': name, 'args':full_caps }, **kwargs)

    def osd_crush_remove(self, name, ancestor = None, **kwargs):
        if ancestor is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd crush remove', 'name': name, 'ancestor': ancestor}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd crush remove', 'name': name}, **kwargs)

    def osd_crush_reweight(self, name, weight, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_rm(self, name, ancestor, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_rule_create_simple(self, name, root, type, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_rule_rm(self, name, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd crush rule rm', 'name': name}, **kwargs)

    def osd_crush_set(self, id, name, weight, args, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_tunables(self, profile, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_crush_unlink(self, name, ancestor, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_deep_scrub(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_down(self, ids, **kwargs):
        if not isinstance(ids, list):
            ids = [temp_id for temp_id in ids.strip().split(" ") if temp_id]
        return self.post('request?wait=1', json = {'prefix': 'osd down', 'ids': ids}, **kwargs)

    def osd_in(self, ids, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_lost(self, id, sure, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_out(self, ids, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_pool_create(self, pool, pg_num, pgp_num = None, pool_type = None, erasure_code_profile = None, ruleset = None, expected_num_objects = None, **kwargs):
        jsont = dict()
        jsont['prefix'] = 'osd pool create'
        jsont['pool'] = pool
        jsont['pg_num'] = pg_num

        if pgp_num is not None:
            jsont['pgp_num'] = pgp_num
        if pool_type is not None:
            jsont['pool_type'] = pool_type
        if erasure_code_profile is not None:
            jsont['erasure_code_profile'] = erasure_code_profile
        if ruleset is not None:
            jsont['rule'] = ruleset
        if expected_num_objects is not None:
            jsont['expected_num_objects'] = expected_num_objects
        return self.post('request?wait=1', json = jsont, **kwargs)

    def osd_pool_delete(self, pool, pool2 = None, sure = None, **kwargs):
        jsont = dict()
        jsont['prefix'] = 'osd pool delete'
        if pool2 is not None:
            jsont['pool2'] = pool2
        if sure is not None:
            jsont['sure'] = sure
        return self.post('request?wait=1', json = jsont, **kwargs)

    def osd_pool_param(self, pool, var, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_pool_mksnap(self, pool, snap, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_pool_rename(self, srcpool, destpool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_pool_rmsnap(self, pool, snap, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_set_pool_param(self, pool, var, val, force = None, **kwargs):
        return self.osd_pool_set(pool, var, val, force, **kwargs)

    def osd_pool_set(self, pool, var, val, force = None, **kwargs):
        if force is not None:
            return self.post('request?wait=1', json = {'prefix': 'osd pool set', 'pool': pool, 'var': var, 'val': val, 'force': force}, **kwargs)
        else:
            return self.post('request?wait=1', json = {'prefix': 'osd pool set', 'pool': pool, 'var': var, 'val': val}, **kwargs)

    def osd_set_pool_quota(self, pool, field, val, **kwargs):
        return self.osd_pool_set_quota(pool, field, val, **kwargs)

    def osd_pool_set_quota(self, pool, field, val, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd pool set-quota', 'pool': pool, 'field': field, 'val': val}, **kwargs)

    def osd_repair(self, pool, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_reweight(self, id, weight, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_reweight_by_utilization(self, oload, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_remove(self, ids, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_scrub(self, who, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_set_key(self, key, **kwargs):
        return self.post('request?wait=1', json = {'prefix': 'osd set', 'key': key}, **kwargs)

    def osd_setmaxosd(self, newmax, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_thrash(self, num_epochs, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_tier_add(self, pool, tierpool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_tier_cachemode(self, pool, mode, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_tier_remove(self, pool, tierpool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_tier_remove_overlay(self, pool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_tier_set_overlay(self, pool, overlaypool, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def osd_unset(self, key, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # pg GET calls
    ###
    def pg_debug(self, debugop, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_dump(self, dumpcontents=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_dump_json(self, dumpcontents=None, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_dump_pools_json(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_dump_stuck(self, stuckops=None, threshold=None, **kwargs):
        jsont = dict()
        jsont['prefix'] = 'pg dump_stuck'
        if stuckops is not None:
            jsont['stuckops'] = stuckops
        if threshold is not None:
            jsont['threshold'] = threshold
	return self.post('request?wait=1', json = jsont, **kwargs)

    def pg_getmap(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_map(self, pgid, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def pg_stat(self, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    ###
    # tell GET calls
    ###
    def tell_debug_dump_missing(self, id, filename, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def tell_dump_pg_recovery_stats(self, id, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def tell_list_missing(self, id, offset, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def tell_query(self, id, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()

    def tell_version(self, id, **kwargs):
        #TODO: force raise exception
        raise exceptions.FunctionNotImplemented()
