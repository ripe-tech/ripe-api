#!/usr/bin/python
# -*- coding: utf-8 -*-

class SizeAPI(object):

    def get_sizes(self):
        url = self.base_url + "sizes"
        contents = self.get(url)
        return contents

    def size_to_native(self,  scale, value, gender, *args, **kwargs):
        url = self.base_url + "sizes/size_to_native?scale=%s&value=%s&gender=%s" % (scale, value, gender)
        contents = self.get(url, auth = False, **kwargs)
        return contents

    def native_to_size(self, scale, value, gender, *args, **kwargs):
        url = self.base_url + "sizes/native_to_size?scale=%s&value=%s&gender=%s" % (scale, value, gender)
        contents = self.get(url, auth = False)
        return contents
