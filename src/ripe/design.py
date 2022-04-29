#!/usr/bin/python
# -*- coding: utf-8 -*-


class DesignAPI(object):
    def list_designs(self, *args, **kwargs):
        url = self.base_url + "designs"
        contents = self.get(url, auth=False, **kwargs)
        return contents

    def create_design(self, design):
        url = self.base_url + "designs"
        contents = self.post(url, auth=False, data_j=design)
        return contents

    def get_design(self, id):
        url = self.base_url + "designs/%d" % id
        contents = self.get(url, auth=False)
        return contents
