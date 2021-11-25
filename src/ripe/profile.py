#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class ProfileAPI(object):

    def get_profiles(self, *args, **kwargs):
        url = self.base_url + "profiles"
        contents = self.get(url, **kwargs)
        return contents

    def get_profile(self, name):
        url = self.base_url + "profiles/%s" % name
        contents = self.get(url)
        return contents
