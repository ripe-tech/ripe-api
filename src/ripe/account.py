#!/usr/bin/python
# -*- coding: utf-8 -*-


class AccountAPI(object):
    def self_account(self, *args, **kwargs):
        url = self.base_url + "accounts/me"
        contents = self.get(url, **kwargs)
        return contents

    def tenancy_account(self, *args, **kwargs):
        url = self.base_url + "accounts/me/tenancy"
        contents = self.get(url, **kwargs)
        return contents
