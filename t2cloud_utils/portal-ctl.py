#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import urllib3
import sys
import json
import subprocess
import requests
import functools


urllib3.disable_warnings()
NUM_THREADS = 10


def execute(cmd, shell=True):
    try:
        output = subprocess.check_output(cmd, shell=shell)
    except subprocess.CalledProcessError:
        return None
    return output


def safe_connect(f):
    @functools.wraps(f)
    def wrapper(self, *a, **k):
        try:
            return f(self, *a, **k)
        except requests.exceptions.ConnectionError as e:
            print('Placement API service is not responding.')
            raise
    return wrapper


class PortalClient(object):
    def __init__(self, url=None, username='admin', password=None):
        if not url:
            raise('Portal url not config')
        self.username = username
        self.password = password
        self.base_url = url
        print(self.base_url, self.username, self.password)
        self.login_url = "%s/portal/auth/login" % url
        self.headers = {
            # 'X-Access-Module': 'ADMIN',
            # 'X-Service-Login': 'TRUE'
        }
        self.license_sn_file = "/tmp/license.sn"
        self.session = requests.Session()
        self.session.verify = False
        self.login()

    @safe_connect
    def login(self):
        payload = {
            'username': self.username,
            'password': self.password,
            'verify_code': None
        }
        res = self.session.post(
                self.login_url, data=payload, headers=self.headers)
        if res.status_code == 200:
            print('Login success.')
        else:
            print('Login Failed. status=%s res=%s' % (
                  res.status_code, res.text))
            raise

    def _check_status_code(self, url, code):
        if code == 401:
            self.login()
            msg = '%s request unauthorized' % url
            print(msg)
            raise
        elif code in [503, 504]:
            msg = '%s request timeout' % url
            print(msg)
            raise
        elif code not in [200, 304]:
            msg = 'Failed to request dspace: %s, code %d' % (url, code)
            print(msg)
            raise

    def get_license_sn(self):
        url = self.base_url + '/portal/api/licenses/download_licenses'
        print(url)
        rsp = self.session.get(url=url, headers=self.headers)
        with open(self.license_sn_file, "wb") as code:
            code.write(json.loads(rsp.text).get('data'))
        print(rsp.status_code, rsp.content.decode("utf-8"))

    def overview(self):
        url = self.base_url + '/portal/api/overview/admin/overview'
        print(url)
        rsp = self.session.get(url=url, headers=self.headers)
        print(rsp.status_code, rsp.content.decode("utf-8"))

    def graph_info(self):
        url = self.base_url + '/portal/api/monitors/graph_info'
        print(url)
        params = {
            "instance_id": "94e8779d-037d-4b73-9f16-fae024b01ff9",
            "period": "HOUR",
            "meters": "CPU_USAGE,MEM_USAGE,NET_SPEED,DISK_READ_WRITE,DISK_IOPS,DISK_USAGE",
            "monitor_type": "REALTIME"
        }
        rsp = self.session.post(url=url, headers=self.headers, data=params)
        print(rsp.status_code, rsp.content.decode("utf-8"))

    def networks(self):
        url = self.base_url + '/portal/api/networks/private_networks'
        print(url)
        rsp = self.session.get(url=url, headers=self.headers)
        print(rsp.status_code, rsp.content.decode("utf-8"))

    def catalog(self):
        url = self.base_url + '/portal/api/instances/catalog/list_catalog'
        print(url)
        print(self.session.cookies)
        rsp = self.session.get(url=url, headers=self.headers)
        print(rsp.status_code, rsp.content.decode("utf-8"))

    def api(self):
        url = self.base_url + '/portal/api/'
        print(url)
        rsp = self.session.get(url=url, headers=self.headers)
        print(rsp.status_code, rsp.content.decode("utf-8"))


if __name__ == '__main__':
    # exec_name = sys.argv.pop(0)
    # if len(sys.argv) < 1:
    #     sys.stderr.write("{}: <url> <admin_password> \n".format(exec_name))
    #     sys.exit(-1)

    # url = 'https://{}'.format(sys.argv[0])
    #  url = 'http://{}:9090'.format(sys.argv[0])
    #  url = 'http://{}:16280'.format(sys.argv[0])
    #  password = '!QAZ2wsx'
    # if len(sys.argv) == 2:
    #     password = sys.argv[1]
    #
    username = 'lwy01@cloud.com'
    password = '!QAZ2wsx'
    url = 'https://192.168.18.128'
    portal = PortalClient(url=url, username=username, password=password)
    #  portal.api()
    #  portal.get_license_sn()
    for i in range(1):
        print(i)
        #portal.overview()
        #portal.api()
        portal.networks()
        #portal.graph_info()
        # portal.catalog()
