#!/usr/bin/python
# -*- coding: utf-8 -*-


class AvailabilityRuleAPI(object):
    def list_availability_rules(self, *args, **kwargs):
        url = self.base_url + "availability_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_availability_rule(self, availability_rule):
        url = self.base_url + "availability_rules"
        contents = self.post(url, data_j=availability_rule)
        return contents

    def get_availability_rule(self, id):
        url = self.base_url + "availability_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_availability_rule(self, id, availability_rule):
        url = self.base_url + "availability_rules/%d" % id
        contents = self.put(url, data_j=availability_rule)
        return contents

    def delete_availability_rule(self, id):
        url = self.base_url + "availability_rules/%d" % id
        contents = self.delete(url)
        return contents
