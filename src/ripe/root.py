#!/usr/bin/python
# -*- coding: utf-8 -*-


class RootAPI(object):
    def geo_resolve(self):
        url = self.base_url + "geo_resolve"
        contents = self.get(url)
        return contents

    def structure(self):
        url = self.base_url + "structure"
        contents = self.get(url)
        return contents

    def thumb(self, model, *args, **kwargs):
        url = self.base_url + "thumb/%s" % model
        contents = self.get(url, **kwargs)
        return contents

    def translate(self, *args, **kwargs):
        url = self.base_url + "translate"
        contents = self.get(url, **kwargs)
        return contents

    def compose(self, *args, **kwargs):
        url = self.base_url + "compose"
        contents = self.get(url, **kwargs)
        return contents

    def mask(self, *args, **kwargs):
        url = self.base_url + "mask"
        contents = self.get(url, **kwargs)
        return contents

    def swatch(self, *args, **kwargs):
        url = self.base_url + "swatch"
        contents = self.get(url, auth=False, **kwargs)
        return contents
