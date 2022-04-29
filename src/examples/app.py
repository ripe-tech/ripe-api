#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import base


class RipeApp(appier.WebApp):
    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(self, name="ripe", *args, **kwargs)

    @appier.route("/", "GET")
    def index(self):
        return self.config()

    @appier.route("/config", "GET")
    def config(self):
        api = self.get_api()
        config = api.get_config()
        return config

    def get_api(self):
        return base.get_api()


if __name__ == "__main__":
    app = RipeApp()
    app.serve()
else:
    __path__ = []
