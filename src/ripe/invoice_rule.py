#!/usr/bin/python
# -*- coding: utf-8 -*-

class InvoiceRuleAPI(object):

    def list_invoice_rules(self, *args, **kwargs):
        url = self.base_url + "invoice_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_invoice_rule(self, invoice_rule):
        url = self.base_url + "invoice_rules"
        contents = self.post(url, data_j = invoice_rule)
        return contents

    def get_invoice_rule(self, id):
        url = self.base_url + "invoice_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_invoice_rule(self, id, invoice_rule):
        url = self.base_url + "invoice_rules/%d" % id
        contents = self.put(url, data_j = invoice_rule)
        return contents

    def delete_invoice_rule(self, id):
        url = self.base_url + "invoice_rules/%d" % id
        contents = self.delete(url)
        return contents
