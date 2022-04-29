#!/usr/bin/python
# -*- coding: utf-8 -*-


class BulkOrderAPI(object):
    def get_bulk_orders(self, **kwargs):
        url = self.base_url + "bulk_orders"
        contents = self.get(url, **kwargs)
        return contents

    def get_bulk_order(self, number):
        url = self.base_url + "bulk_orders/%d" % number
        contents = self.get(url)
        return contents

    def set_bulk_order_status(self, number, status, **kwargs):
        url = self.base_url + "bulk_orders/%d/%s" % (number, status)
        contents = self.put(url, **kwargs)
        return contents

    def create_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "create", **kwargs)

    def produce_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "produce", **kwargs)

    def quality_assure_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "quality_assure", **kwargs)

    def reject_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "reject", **kwargs)

    def ready_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "ready", **kwargs)

    def send_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "send", **kwargs)

    def block_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "block", **kwargs)

    def receive_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "receive", **kwargs)

    def return_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "return", **kwargs)

    def cancel_bulk_order(self, number, **kwargs):
        return self.set_bulk_order_status(number, "cancel", **kwargs)

    def import_bulk_order(self, name, orders, **kwargs):
        url = self.base_url + "bulk_orders"
        brand = kwargs.get("brand", None)
        description = kwargs.get("description", None)
        data_j = dict(name=name, orders=orders)
        if brand:
            data_j["brand"] = brand
        if description:
            data_j["description"] = description
        contents = self.post(url, data_j=data_j, **kwargs)
        return contents

    def attachments_bulk_order(self, number):
        url = self.base_url + "bulk_orders/%d/attachments" % number
        contents = self.get(url)
        return contents

    def create_attachment_bulk_order(self, number, files, **kwargs):
        url = self.base_url + "bulk_orders/%d/attachments" % number
        data_m = dict(files=files)
        contents = self.post(url, data_m=data_m, **kwargs)
        return contents
