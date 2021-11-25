#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import account
from . import brand
from . import build
from . import config
from . import country_group
from . import design
from . import justification
from . import locale
from . import model
from . import notify_info
from . import order
from . import profile
from . import size
from . import sku

RIPE_BASE_URL = "http://localhost/api/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """

class API(
    account.AccountAPI,
    appier.API,
    config.ConfigAPI,
    country_group.CountryGroupAPI,
    brand.BrandAPI,
    build.BuildAPI,
    design.DesignAPI,
    justification.JustificationAPI,
    locale.LocaleAPI,
    model.ModelAPI,
    notify_info.NotifyInfoAPI,
    order.OrderAPI,
    profile.ProfileAPI,
    size.SizeAPI,
    sku.SkuAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("RIPE_BASE_URL", RIPE_BASE_URL)
        self.username = appier.conf("RIPE_USERNAME", None)
        self.password = appier.conf("RIPE_PASSWORD", None)
        self.secret_key = appier.conf("RIPE_SECRET_KEY", None)
        self.admin = appier.conf("RIPE_ADMIN", True, cast = bool)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self.secret_key = kwargs.get("secret_key", self.secret_key)
        self.admin = kwargs.get("admin", self.admin)
        self.session_id = kwargs.get("session_id", None)
        self.token = kwargs.get("token", None)
        self.key = kwargs.get("key", None)
        self.login_mode = kwargs.get("login_mode", None)

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
        if auth and self.secret_key: headers["X-Secret-Key"] = self.secret_key
        if auth and not self.secret_key: params["sid"] = self.get_session_id()

    def get_session_id(self):
        if self.session_id: return self.session_id
        if self.login_mode == "pid": return self.login_pid()
        if self.key == "key": return self.login_key()
        return self.login()

    def auth_callback(self, params, headers):
        self.session_id = None
        session_id = self.get_session_id()
        params["sid"] = session_id

    def login(self, username = None, password = None, admin = None, token = None):
        self.login_mode = "username"
        username = username or self.username
        password = password or self.password
        admin = admin or self.admin
        token = token or self.token
        if token: return self.login_pid(token = token)
        url = self.base_url + ("signin_admin" if admin else "signin")
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
        self.password = password
        self.trigger("auth", contents)
        return self.session_id

    def login_pid(self, token = None):
        self.login_mode = "pid"
        token = token or self.token
        url = self.base_url + "signin_pid"
        contents = self.post(
            url,
            callback = False,
            auth = False,
            token = token
        )
        self.username = contents.get("username", None)
        self.session_id = contents.get("session_id", None)
        self.tokens = contents.get("tokens", None)
        self.token = token
        self.trigger("auth", contents)
        return self.session_id

    def is_auth(self):
        if not self.username: return False
        if not self.password: return False
        return True

    def login_key(self, key = None):
        self.login_mode = "pid"
        key = key or self.key
        url = self.base_url + "signin_key"
        contents = self.post(
            url,
            callback = False,
            auth = False,
            key = key
        )
        self.username = contents.get("username", None)
        self.session_id = contents.get("session_id", None)
        self.tokens = contents.get("tokens", None)
        self.key = key
        self.trigger("auth", contents)
        return self.session_id

    def ping(self):
        url = self.base_url + "ping"
        contents = self.get(url)
        return contents

    def geo_resolve(self):
        url = self.base_url + "geo_resolve"
        contents = self.get(url)
        return contents

    def structure(self):
        url = self.base_url + "structure"
        contents = self.get(url)
        return contents

    def thumb(self, model, *args, **kwargs):
        url = self.base_url + "thumb/%s" % model
        contents = self.get(url, **kwargs)
        return contents

    def translate(self, *args, **kwargs):
        url = self.base_url + "translate"
        contents = self.get(url, **kwargs)
        return contents

    def compose(self, *args, **kwargs):
        url = self.base_url + "compose"
        contents = self.get(url, **kwargs)
        return contents

    def mask(self, *args, **kwargs):
        url = self.base_url + "mask"
        contents = self.get(url, **kwargs)
        return contents

    def swatch(self, *args, **kwargs):
        url = self.base_url + "swatch"
        contents = self.get(url, auth = False, **kwargs)
        return contents

    def clear_cache_compose(self):
        url = self.base_url + "compose/clear"
        contents = self.get(url)
        return contents
