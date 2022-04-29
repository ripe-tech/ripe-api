#!/usr/bin/python
# -*- coding: utf-8 -*-


class NotifyInfoAPI(object):
    def create_device_id(self, device_id):
        url = self.base_url + "notify_infos/device_ids"
        contents = self.post(url, data_j=dict(id=device_id))
        return contents

    def remove_device_id(self, device_id):
        url = self.base_url + "notify_infos/device_ids/%s" % device_id
        contents = self.delete(url)
        return contents
