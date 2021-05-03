#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class OrderAPI(object):

    @classmethod
    def load_order(cls, order):
        structure = order.get("structure", None)
        if structure: order["details"] = json.loads(structure)
        else: order["details"] = dict()
        return order

    def list_orders(self, *args, **kwargs):
        url = self.base_url + "orders"
        contents = self.get(url, **kwargs)
        return contents

    def create_order(self, order):
        url = self.base_url + "orders"
        contents = self.post(url, data_j = order)
        return contents

    def get_order(self, number):
        url = self.base_url + "orders/%d" % number
        contents = self.get(url)
        return contents

    def delete_order(self, number):
        url = self.base_url + "orders/%d" % number
        contents = self.delete(url)
        return contents

    def price_order(self, number, currency = None):
        url = self.base_url + "orders/%d/price" % number
        contents = self.get(url, currency = currency)
        return contents

    def report_pdf(self, number):
        url = self.base_url + "orders/%d/report.pdf" % number
        contents = self.get(url, number)
        return contents

    def import_order(
        self,
        ff_order_id,
        contents,
        currency = None,
        country = None,
        meta = None,
        safe = True,
        notify = False,
        pending = False,
        *args,
        **kwargs
    ):
        url = self.base_url + "orders/import"
        contents = self.post(
            url,
            ff_order_id = ff_order_id,
            contents = contents,
            currency = currency,
            country = country,
            meta = meta,
            safe = safe,
            notify = notify,
            pending = pending,
            **kwargs
        )
        return contents

    def create_farfetch_order(
        self,
        ff_order_id,
        contents,
        currency = None,
        country = None,
        meta = None,
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
            meta = meta,
            safe = safe,
            notify = notify,
            **kwargs
        )
        return contents
