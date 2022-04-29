#!/usr/bin/python
# -*- coding: utf-8 -*-


class VideoAPI(object):
    def video(self, model, name, brand=None, version=None, parts=None):
        url = self.base_url + "video"
        contents = self.get(
            url, data_j=dict(model, name, brand=brand, version=version, p=parts)
        )
        return contents

    def video_thumbnail(self, model, name, brand=None, version=None, parts=None):
        url = self.base_url + "video/thumbnail"
        contents = self.get(
            url, data_j=dict(model, name, brand=brand, version=version, p=parts)
        )
        return contents
