#!/usr/bin/python
# -*- coding: utf-8 -*-


class TransportRuleAPI(object):
    def list_transport_rules(self, *args, **kwargs):
        url = self.base_url + "transport_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_transport_rule(self, transport_rule):
        url = self.base_url + "transport_rules"
        contents = self.post(url, data_j=transport_rule)
        return contents

    def get_transport_rule(self, id):
        url = self.base_url + "transport_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_transport_rule(self, id, transport_rule):
        url = self.base_url + "transport_rules/%d" % id
        contents = self.put(url, data_j=transport_rule)
        return contents

    def delete_transport_rule(self, id):
        url = self.base_url + "transport_rules/%d" % id
        contents = self.delete(url)
        return contents

    def resolve_transport_rule(self, brand=None, model=None, country=None, factory=None):
        url = self.base_url + "transport_rules/resolve"
        contents = self.get(
            url, brand=brand, model=model, country=country, factory=factory
        )
        return contents
