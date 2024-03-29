#!/usr/bin/python
# -*- coding: utf-8 -*-


class LocaleAPI(object):
    def get_locale(self, *args, **kwargs):
        url = self.base_url + "locale"
        contents = self.get(url, **kwargs)
        return contents

    def get_locale_bundle(self, *args, **kwargs):
        url = self.base_url + "locale/bundle"
        contents = self.get(url, **kwargs)
        return contents

    def locale_m_locale(self, values, locale="en-us"):
        url = self.base_url + "locale"
        contents = self.post(url, values=values, locale=locale)
        return contents

    def locale_s_locale(self, value, locale="en-us"):
        url = self.base_url + "locale" + "/" + value
        contents = self.post(url, locale=locale)
        return contents
