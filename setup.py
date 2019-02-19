from setuptools import setup

setup(
    name='client-mgr-restful',
    packages=['mgr_restful_client'],
    version='0.1.0.0',
    url='https://github.com/iotcg/client-mgr-restful',
    author='Changcheng Liu',
    author_email='changcheng.liu@aliyun.com',
    description='Ceph Mgr RESTful plugin python client.',
    long_description=open('README.rst', 'rt').read(),
    license='Apache License, Version 2.0',
    keywords='ceph mgr restful plugin python client',
    install_requires=['requests>=2.2.1'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)
