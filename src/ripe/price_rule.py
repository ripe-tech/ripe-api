#!/usr/bin/python
# -*- coding: utf-8 -*-


class PriceRuleAPI(object):
    def list_price_rules(self, *args, **kwargs):
        url = self.base_url + "price_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_price_rule(self, price_rule):
        url = self.base_url + "price_rules"
        contents = self.post(url, data_j=price_rule)
        return contents

    def get_price_rule(self, id):
        url = self.base_url + "price_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_price_rule(self, id, price_rule):
        url = self.base_url + "price_rules/%d" % id
        contents = self.put(url, data_j=price_rule)
        return contents

    def delete_price_rule(self, id):
        url = self.base_url + "price_rules/%d" % id
        contents = self.delete(url)
        return contents
