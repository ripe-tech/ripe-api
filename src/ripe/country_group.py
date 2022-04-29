#!/usr/bin/python
# -*- coding: utf-8 -*-


class CountryGroupAPI(object):
    def list_country_groups(self, *args, **kwargs):
        url = self.base_url + "country_groups"
        contents = self.get(url, **kwargs)
        return contents

    def create_country_group(self, country_group):
        url = self.base_url + "country_groups"
        contents = self.post(url, data_j=country_group)
        return contents

    def get_country_group(self, id):
        url = self.base_url + "country_groups/%d" % id
        contents = self.get(url)
        return contents

    def update_country_group(self, id, country_group):
        url = self.base_url + "country_groups/%d" % id
        contents = self.put(url, data_j=country_group)
        return contents

    def delete_country_group(self, id):
        url = self.base_url + "country_groups/%d" % id
        contents = self.delete(url)
        return contents
