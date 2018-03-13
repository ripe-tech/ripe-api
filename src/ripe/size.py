#!/usr/bin/python
# -*- coding: utf-8 -*-

class SizeAPI(object):

    def get_sizes(self):
        url = self.base_url + "sizes"
        contents = self.get(url)
        return contents

    def size_to_native(self,  scale, value, gender, *args, **kwargs):
        url = self.base_url + "sizes/size_to_native"
        contents = self.get(
            url, 
            auth = False,
            scale = scale,
            value = value,
            gender = gender,
            **kwargs
        )
        return contents

    def native_to_size(self, scale, value, gender, *args, **kwargs):
        url = self.base_url + "sizes/native_to_size"
        contents = self.get(
            url, 
            auth = False,
            scale = scale,
            value = value,
            gender = gender,
            **kwargs
        )
        return contents
