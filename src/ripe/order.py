#!/usr/bin/python
# -*- coding: utf-8 -*-

class OrderAPI(object):

    def list_orders(self, *args, **kwargs):
        url = self.base_url + "orders"
        contents = self.get(url, **kwargs)
        return contents

    def create_order(self, order):
        url = self.base_url + "orders"
        contents = self.post(url, data_j = order)
        return contents

    def create_farfetch_order(
        self,
        ff_order_id,
        contents,
        currency = None,
        country = None,
        safe = True,
        notify = False,
        *args,
        **kwargs
    ):
        url = self.base_url + "orders/farfetch"
        contents = self.post(
            url,
            ff_order_id = ff_order_id,
            contents = contents,
            currency = currency,
            country = country,
            safe = safe,
            notify = notify,
            **kwargs
        )
        return contents
