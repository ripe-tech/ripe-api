#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import model
from . import order
from . import config

RIPE_CORE_BASE_URL = "http://localhost/api/"
""" The default base url to be used when no other
base url value is provided to the constructor """

class Api(
    appier.Api,
    model.ModelApi,
    order.OrderApi,
    config.ConfigApi
):

    def __init__(self, *args, **kwargs):
        appier.Api.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("RIPE_BASE_URL", RIPE_CORE_BASE_URL)
        self.username = appier.conf("RIPE_USERNAME", None)
        self.password = appier.conf("RIPE_PASSWORD", None)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self.session_id = kwargs.get("session_id", None)

    def build(
        self,
        method,
        url,
        data = None,
        data_j = None,
        data_m = None,
        headers = None,
        params = None,
        mime = None,
        kwargs = None
    ):
        auth = kwargs.pop("auth", True)
        if auth: params["sid"] = self.get_session_id()

    def get_session_id(self):
        if self.session_id: return self.session_id
        return self.login()

    def auth_callback(self, params, headers):
        self.session_id = None
        session_id = self.get_session_id()
        params["session_id"] = session_id

    def login(self, username = None, password = None):
        username = username or self.username
        password = password or self.password
        url = self.base_url + "admin/login"
        contents = self.post(
            url,
            callback = False,
            auth = False,
            username = username,
            password = password
        )
        self.username = contents.get("username", None)
        self.session_id = contents.get("session_id", None)
        self.tokens = contents.get("tokens", None)
        self.trigger("auth", contents)
        return self.session_id

    def is_auth(self):
        if not self.username: return False
        if not self.password: return False
        return True
