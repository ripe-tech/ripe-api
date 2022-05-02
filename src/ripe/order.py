#!/usr/bin/python
# -*- coding: utf-8 -*-

import json


class OrderAPI(object):
    @classmethod
    def load_order(cls, order):
        structure = order.get("structure", None)
        if structure:
            order["details"] = json.loads(structure)
        else:
            order["details"] = dict()
        return order

    def list_orders(self, *args, **kwargs):
        url = self.base_url + "orders"
        contents = self.get(url, **kwargs)
        return contents

    def create_order(self, order):
        url = self.base_url + "orders"
        contents = self.post(url, data_j=order)
        return contents

    def get_order(self, number):
        url = self.base_url + "orders/%d" % number
        contents = self.get(url)
        return contents

    def transport_order(self, number):
        url = self.base_url + "orders/%d/transport" % number
        contents = self.get(url)
        return contents

    def attachments_order(self, number, *args, **kwargs):
        url = self.base_url + "orders/%d/attachments" % number
        contents = self.get(url, **kwargs)
        return contents

    def create_attachments_order(self, number, file):
        url = self.base_url + "orders/%d/attachments" % number
        contents = self.post(url, data_j=file)
        return contents

    def attachment_order(self, number, attachment_id):
        url = self.base_url + "orders/%d/attachments/%d" % (number, attachment_id)
        contents = self.get(url)
        return contents

    def create_note_order(self, number, note):
        url = self.base_url + "orders/%d/notes" % number
        contents = self.post(url, data_j=note)
        return contents

    def create_waybill_order(self, number):
        url = self.base_url + "orders/%d/waybill" % number
        contents = self.post(url)
        return contents

    def create_return_waybill_order(self, number):
        url = self.base_url + "orders/%d/return_waybill" % number
        contents = self.post(url)
        return contents

    def void_waybill_order(self, number):
        url = self.base_url + "orders/%d/waybill" % number
        contents = self.delete(url)
        return contents

    def void_return_waybill_order(self, number):
        url = self.base_url + "orders/%d/return_waybill" % number
        contents = self.delete(url)
        return contents

    def refresh_shipping_order(self, number):
        url = self.base_url + "orders/%d/refresh_shipping" % number
        contents = self.post(url)
        return contents

    def log_order(self, number):
        url = self.base_url + "orders/%d/log" % number
        contents = self.get(url)
        return contents

    def chat_order(self, number):
        url = self.base_url + "orders/%d/chat" % number
        contents = self.get(url)
        return contents

    def chat_lines_order(self, number, *args, **kwargs):
        url = self.base_url + "orders/%d/chat/lines" % number
        contents = self.get(url, **kwargs)
        return contents

    def chat_lines_count_order(self, number):
        url = self.base_url + "orders/%d/chat/lines/count" % number
        contents = self.get(url)
        return contents

    def chat_create_line_order(self, number, content):
        url = self.base_url + "orders/%d/chat/lines/count" % number
        contents = self.post(url, data_j=content)
        return contents

    def states_order(self, number):
        url = self.base_url + "orders/%d/states" % number
        contents = self.get(url)
        return contents

    def state_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_chat_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d/chat" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_chat_lines_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d/chat/lines" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_chat_lines_count_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d/chat/lines/count" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_chat_create_line_order(self, number, state_id, content):
        url = self.base_url + "orders/%d/states/%d/chat/lines/count" % (number, state_id)
        contents = self.post(url, data_j=content)
        return contents

    def state_attachments_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d/attachments" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_attachments_count_order(self, number, state_id):
        url = self.base_url + "orders/%d/states/%d/attachments/count" % (number, state_id)
        contents = self.get(url)
        return contents

    def state_create_attachments_order(self, number, state_id, file):
        url = self.base_url + "orders/%d/states/%d/attachments" % (number, state_id)
        contents = self.post(url, data_j=file)
        return contents

    def state_attachment_order(self, number, state_id, attachment_id):
        url = self.base_url + "orders/%d/states/%d/attachments/%d" % (
            number,
            state_id,
            attachment_id,
        )
        contents = self.get(url)
        return contents

    def set_meta_order(self, number, key, value):
        url = self.base_url + "orders/%d/meta" % number
        contents = self.put(url, data_j=dict(key=key, value=value))
        return contents

    def set_priority_order(self, number, priority):
        url = self.base_url + "orders/%d/priority" % number
        contents = self.put(url, priority=priority)
        return contents

    def set_tracking_order(self, number, tracking_number, tracking_url):
        url = self.base_url + "orders/%d/tracking" % number
        contents = self.put(
            url, tracking_number=tracking_number, tracking_url=tracking_url
        )
        return contents

    def set_return_tracking_order(
        self, number, return_tracking_number, return_tracking_url
    ):
        url = self.base_url + "orders/%d/return_tracking" % number
        contents = self.put(
            url,
            return_tracking_number=return_tracking_number,
            return_tracking_url=return_tracking_url,
        )
        return contents

    def unset_tracking_order(self, number):
        url = self.base_url + "orders/%d/tracking" % number
        contents = self.delete(url)
        return contents

    def unset_return_tracking_order(self, number):
        url = self.base_url + "orders/%d/return_tracking" % number
        contents = self.delete(url)
        return contents

    def precustomization_order(self, number, tracking_number, tracking_url):
        url = self.base_url + "orders/%d/tracking" % number
        contents = self.put(
            url, tracking_number=tracking_number, tracking_url=tracking_url
        )
        return contents

    def get_subscription_order(self, number):
        url = self.base_url + "orders/%d/subscription" % number
        contents = self.get(url)
        return contents

    def subscribe_order(self, number):
        url = self.base_url + "orders/%d/subscription" % number
        contents = self.put(url)
        return contents

    def unsubscribe_order(self, number):
        url = self.base_url + "orders/%d/subscription" % number
        contents = self.delete(url)
        return contents

    def update_report_url_order(self, number, report_url):
        url = self.base_url + "orders/%d/report_url" % number
        contents = self.put(url, report_url=report_url)
        return contents

    def search_order(self, *args, **kwargs):
        url = self.base_url + "orders/search"
        contents = self.get(url)
        return contents

    def delete_order(self, number):
        url = self.base_url + "orders/%d" % number
        contents = self.delete(url)
        return contents

    def price_order(self, number, currency=None):
        url = self.base_url + "orders/%d/price" % number
        contents = self.get(url, currency=currency)
        return contents

    def produce_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/produce" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def quality_assure_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/quality_assure" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def reject_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/reject" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def ready_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/ready" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def send_order(
        self,
        number,
        justification=None,
        notify=False,
        strict=True,
        tracking_number=None,
        tracking_url=None,
    ):
        url = self.base_url + "orders/%d/send" % number
        contents = self.put(
            url,
            justification=justification,
            notify=notify,
            strict=strict,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
        )
        return contents

    def block_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/block" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def receive_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/receive" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def return_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/return" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def cancel_order(self, number, justification=None, notify=False, strict=True):
        url = self.base_url + "orders/%d/cancel" % number
        contents = self.put(
            url, justification=justification, notify=notify, strict=strict
        )
        return contents

    def report_pdf(self, number, key):
        url = self.base_url + "orders/%d/report.pdf" % number
        contents = self.get(url, key=key)
        return contents

    def update_tag(self, number, identifier=None, type=None, activate=None):
        url = self.base_url + "orders/%d/tag" % number
        contents = self.put(url, identifier=identifier, type=type, activate=activate)
        return contents

    def activate_tag(self, number):
        url = self.base_url + "orders/%d/tag/activate" % number
        contents = self.put(url)
        return contents

    def import_order(
        self,
        ff_order_id,
        contents,
        currency=None,
        country=None,
        meta=None,
        safe=True,
        notify=False,
        pending=False,
        *args,
        **kwargs
    ):
        url = self.base_url + "orders/import"
        contents = self.post(
            url,
            ff_order_id=ff_order_id,
            contents=contents,
            currency=currency,
            country=country,
            meta=meta,
            safe=safe,
            notify=notify,
            pending=pending,
            **kwargs
        )
        return contents

    def create_farfetch_order(
        self,
        ff_order_id,
        contents,
        currency=None,
        country=None,
        meta=None,
        safe=True,
        notify=False,
        *args,
        **kwargs
    ):
        url = self.base_url + "orders/farfetch"
        contents = self.post(
            url,
            ff_order_id=ff_order_id,
            contents=contents,
            currency=currency,
            country=country,
            meta=meta,
            safe=safe,
            notify=notify,
            **kwargs
        )
        return contents
