#!/usr/bin/python
# -*- coding: utf-8 -*-

class OrderApi(object):

    def list_orders(self, *args, **kwargs):
        url = self.base_url + "orders"
        contents = self.get(url, **kwargs)
        return contents

    def create_order(self, order):
        url = self.base_url + "orders"
        contents = self.post(url, data_j = order)
        return contents
