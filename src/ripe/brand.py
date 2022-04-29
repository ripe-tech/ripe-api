#!/usr/bin/python
# -*- coding: utf-8 -*-


class BrandAPI(object):
    def logo_brand(self, brand, model, format="png", size=None):
        url = self.base_url + "brands/%s/models/%s/logo.%s" % (brand, model, format)
        contents = self.get(url, auth=False, size=size)
        return contents

    def mesh_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/mesh" % (brand, model)
        contents = self.get(url, auth=False)
        return contents

    def config_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/config" % (brand, model)
        contents = self.get(url, auth=False)
        return contents

    def defaults_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/defaults" % (brand, model)
        contents = self.get(url, auth=False)
        return contents

    def combinations_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/combinations" % (brand, model)
        contents = self.get(url, auth=False)
        return contents

    def factory_brand(self, brand, model):
        url = self.base_url + "brands/%s/models/%s/factory" % (brand, model)
        contents = self.get(url, auth=False)
        return contents

    def validate_brand(self, brand, model, *args, **kwargs):
        url = self.base_url + "brands/%s/models/%s/validate" % (brand, model)
        contents = self.get(url, auth=False, **kwargs)
        return contents

    def logic_method_brand(self, brand, model, method, version=None, data_j=None):
        url = self.base_url + "brands/%s/models/%s/logic/%s" % (brand, model, method)
        contents = self.post(
            url,
            auth=False,
            params=dict(version=version) if version else dict(),
            data_j=data_j,
        )
        return contents

    def logic_exists_brand(self, brand, model, method, version=None):
        url = self.base_url + "brands/%s/models/%s/logic/%s/exists" % (
            brand,
            model,
            method,
        )
        contents = self.get(
            url, auth=False, params=dict(version=version) if version else dict()
        )
        return contents
