#!/usr/bin/python
# -*- coding: utf-8 -*-

class BuildAPI(object):

    def list_builds(self):
        url = self.base_url + "builds"
        contents = self.get(url)
        return contents

    def list_local_builds(self, *args, **kwargs):
        url = self.base_url + "builds/local"
        contents = self.get(url, **kwargs)
        return contents

    def get_build(self, build, *args, **kwargs):
        url = self.base_url + "builds/%s" % build
        contents = self.get(url, **kwargs)
        return contents

    def install_build(self, name, *args, **kwargs):
        url = self.base_url + "builds/%s/install" % name
        contents = self.put(url, **kwargs)
        return contents

    def uninstall_build(self, name, *args, **kwargs):
        url = self.base_url + "builds/%s/uninstall" % name
        contents = self.put(url, **kwargs)
        return contents

    def update_build(self, name, *args, **kwargs):
        url = self.base_url + "builds/%s/update" % name
        contents = self.put(url, **kwargs)
        return contents

    def switch_build(self, name, *args, **kwargs):
        url = self.base_url + "builds/%s/switch" % name
        contents = self.put(url, **kwargs)
        return contents

    def list_build_artifacts(self, name, *args, **kwargs):
        url = self.base_url + "builds/%s/artifacts" % name
        contents = self.get(url, **kwargs)
        return contents

    def get_build_artifact(self, name, version, *args, **kwargs):
        url = self.base_url + "builds/%s/artifacts/%s" % (name, version)
        contents = self.get(url, **kwargs)
        return contents

    def install_artifact(self, name, version, *args, **kwargs):
        url = self.base_url + "builds/%s/artifacts/%s/install" % (name, version)
        contents = self.get(url, **kwargs)
        return contents

    def uninstall_artifact(self, name, version, *args, **kwargs):
        url = self.base_url + "builds/%s/artifacts/%s/uninstall" % (name, version)
        contents = self.get(url, **kwargs)
        return contents

    def switch_artifact(self, name, version, *args, **kwargs):
        url = self.base_url + "builds/%s/artifacts/%s/switch" % (name, version)
        contents = self.get(url, **kwargs)
        return contents

    def get_locale_model(self, brand, model, locale, *args, **kwargs):
        url = self.base_url + "builds/%s/locale/%s" % (brand, locale)
        contents = self.get(url, model = model, auth = False, **kwargs)
        return contents

    def get_locale_model_keys(self, brand, model, *args, **kwargs):
        url = self.base_url + "builds/%s/locale/keys" % brand
        contents = self.get(url, model = model, **kwargs)
        return contents
