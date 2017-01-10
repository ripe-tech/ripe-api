#!/usr/bin/python
# -*- coding: utf-8 -*-

class ModelApi(object):

    def defaults_model(self, model):
        url = self.base_url + "models/%s/defaults" % model
        contents = self.get(url, auth = False)
        return contents
