#!/usr/bin/python
# -*- coding: utf-8 -*-

class AccountAPI(object):
    
    def account_me(self, *args, **kwargs):
        url = self.base_url + "accounts/me"
        contents = self.get(url, **kwargs)
        return contents

    def tenancy_account_me(self, *args, **kwargs):
        url = self.base_url + "accounts/me/tenancy"
        contents = self.get(url, **kwargs)
        return contents
