#!/usr/bin/python
# -*- coding: utf-8 -*-

class BrandAPI(object):

    def config_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/config" % (brand, model)
        contents = self.get(url, auth = False)
        return contents

    def defaults_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/defaults" % (brand, model)
        contents = self.get(url, auth = False)
        return contents

    def combinations_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/combinations" % (brand, model)
        contents = self.get(url, auth = False)
        return contents

    def validate_brand(self, brand, model, *args, **kwargs):
        url = self.base_url + "brands/%s/models/%s/validate" % (brand, model)
        contents = self.get(url, auth = False, **kwargs)
        return contents
