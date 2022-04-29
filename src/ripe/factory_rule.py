#!/usr/bin/python
# -*- coding: utf-8 -*-


class FactoryRuleAPI(object):
    def list_factory_rules(self, *args, **kwargs):
        url = self.base_url + "factory_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_factory_rule(self, factory_rule):
        url = self.base_url + "factory_rules"
        contents = self.post(url, data_j=factory_rule)
        return contents

    def get_factory_rule(self, id):
        url = self.base_url + "factory_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_factory_rule(self, id, factory_rule):
        url = self.base_url + "factory_rules/%d" % id
        contents = self.put(url, data_j=factory_rule)
        return contents

    def delete_factory_rule(self, id):
        url = self.base_url + "factory_rules/%d" % id
        contents = self.delete(url)
        return contents
