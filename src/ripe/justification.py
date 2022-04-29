#!/usr/bin/python
# -*- coding: utf-8 -*-


class JustificationAPI(object):
    def list_justifications(self, *args, **kwargs):
        url = self.base_url + "justifications"
        contents = self.get(url, **kwargs)
        return contents

    def get_justification(self, context):
        url = self.base_url + "justifications/%s" % context
        contents = self.get(url)
        return contents
