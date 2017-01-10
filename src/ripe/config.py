#!/usr/bin/python
# -*- coding: utf-8 -*-

class ConfigApi(object):

    def get_config(self):
        url = self.base_url + "config"
        contents = self.get(url)
        return contents

    def resolve_config(self, product_id):
        url = self.base_url + "config/resolve/%s" % product_id
        contents = self.get(url, auth = False)
        return contents

    def defaults_model_config(self, model):
        url = self.base_url + "config/defaults/%s" % model
        contents = self.get(url, auth = False)
        return contents
