#!/usr/bin/python
# -*- coding: utf-8 -*-


class ComposeAPI(object):
    def clear_cache_compose(self):
        url = self.base_url + "compose/clear"
        contents = self.get(url)
        return contents
