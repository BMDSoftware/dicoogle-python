#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'dicoogle'
__version__ = '2.0'
__author__ = 'Luís Bastião Silva'
__original_authors__ = 'Luís A. Bastião Silva, Tiago Marques Godinho'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2020, BMD software'

__url__ = 'https://www.dicoogle.com'

__maintainer__ = 'Luís Bastião Silva'
__email__ = 'bastiao@bmd-software.com'

__all__ = ()

import requests

class Dicoogle:
    def __init__(self, url='demo.dicoogle.com'):
        self.ENDPOINT = "http://" + url

    # Validated
    def search_dim(self, query, provider=None, keyword=True):
        url = self.ENDPOINT + "/searchDIM"
        data = {"query": query, "keyword": keyword}
        if provider:
            data["provider"] = provider

        r = requests.get(url, params=data)
        return r

    #Validated
    def export_csv(self, query, fields=[], providers=[], file=None):
        url = self.ENDPOINT + "/export"
        data = {"query": query, "fields": fields, "providers": providers}
        r = requests.get(url, params=data, stream=True)
        if file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()

        return r

    def index(self, uri, provider=None):
        url = self.ENDPOINT + "/management/tasks/index"
        data = {"uri":uri}
        if provider:
            data["provider"] = provider
        r = requests.post(url,data=data)
        return r

    def search(self, query, provider, keyword=False):
        url = self.ENDPOINT + "/search"
        data = {"query": query, "provider": provider, "keyword": keyword}
        r = requests.get(url, params=data);
        return r

    def dump(self, uid):
        url = self.ENDPOINT + "/dump"
        data = {"uid": uid}
        r = requests.get(url, params=data)
        return r
