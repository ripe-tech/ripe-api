#!/usr/bin/python
# -*- coding: utf-8 -*-


class LetterRuleAPI(object):
    def list_letter_rules(self, *args, **kwargs):
        url = self.base_url + "letter_rules"
        contents = self.get(url, **kwargs)
        return contents

    def create_letter_rule(self, letter_rule):
        url = self.base_url + "letter_rules"
        contents = self.post(url, data_j=letter_rule)
        return contents

    def get_letter_rule(self, id):
        url = self.base_url + "letter_rules/%d" % id
        contents = self.get(url)
        return contents

    def update_letter_rule(self, id, letter_rule):
        url = self.base_url + "letter_rules/%d" % id
        contents = self.put(url, data_j=letter_rule)
        return contents

    def delete_letter_rule(self, id):
        url = self.base_url + "letter_rules/%d" % id
        contents = self.delete(url)
        return contents
