#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

from . import sku
from . import root
from . import size
from . import brand
from . import model
from . import order
from . import video
from . import config
from . import design
from . import locale
from . import account
from . import compose
from . import profile
from . import price_rule
from . import letter_rule
from . import notify_info
from . import factory_rule
from . import country_group
from . import justification
from . import transport_rule
from . import availability_rule

RIPE_BASE_URL = "http://localhost/api/"
""" The default base URL to be used when no other
base URL value is provided to the constructor """


class API(
    appier.API,
    sku.SkuAPI,
    root.RootAPI,
    size.SizeAPI,
    brand.BrandAPI,
    model.ModelAPI,
    order.OrderAPI,
    video.VideoAPI,
    config.ConfigAPI,
    design.DesignAPI,
    locale.LocaleAPI,
    account.AccountAPI,
    compose.ComposeAPI,
    profile.ProfileAPI,
    price_rule.PriceRuleAPI,
    letter_rule.LetterRuleAPI,
    notify_info.NotifyInfoAPI,
    factory_rule.FactoryRuleAPI,
    country_group.CountryGroupAPI,
    justification.JustificationAPI,
    transport_rule.TransportRuleAPI,
    availability_rule.AvailabilityRuleAPI,
):
    @classmethod
    def _query_to_spec(cls, query):
        options = cls._unpack_query(query)
        brand = options.get("brand", None)
        model = options.get("model", None)
        variant = options.get("variant", None)
        version = options.get("version", None)
        description = options.get("description", None)
        initials = options.get("initials", None)
        engraving = options.get("engraving", None)
        gender = options.get("gender", None)
        size = options.get("size", None)
        meta = options.get("meta", [])
        tuples = options.get("p", [])
        tuples = tuples if isinstance(tuples, list) else [tuples]
        initials_extra = options.get("initials_extra", [])
        initials_extra = (
            initials_extra if isinstance(initials_extra, list) else [initials_extra]
        )
        initials_extra = cls._parse_extra_s(initials_extra)
        parts = cls._tuples_to_parts(tuples)
        parts_m = cls._parts_to_parts_m(parts)
        spec = dict(
            brand=brand,
            model=model,
            parts=parts_m,
            initials=initials,
            engraving=engraving,
            initials_extra=initials_extra,
        )
        if variant:
            spec["variant"] = variant
        if version:
            spec["version"] = version
        if description:
            spec["description"] = description
        if gender:
            spec["gender"] = gender
        if size:
            spec["size"] = size
        if meta:
            spec["meta"] = cls._normalize_meta(meta)
        return spec

    @classmethod
    def _unpack_query(cls, query):
        query = query.strip("?")
        parts = appier.split_unescape(query, "&")
        options = dict()
        for part in parts:
            key, value = part.split("=")
            if not key in options:
                options[key] = value
            elif isinstance(options[key], list):
                options[key].append(value)
            else:
                options[key] = [options[key], value]
        return options

    @classmethod
    def _parse_extra_s(cls, extra_s):
        extra = dict()
        for extra_i in extra_s:
            name, initials, engraving = appier.split_unescape(extra_i, ":", 2)
            extra[name] = dict(initials=initials, engraving=engraving or None)
        return extra

    @classmethod
    def _tuples_to_parts(cls, tuples):
        parts = []
        for triplet in tuples:
            name, material, color = appier.split_unescape(triplet, ":", 2)
            part = dict(name=name, material=material, color=color)
            parts.append(part)
        return parts

    @classmethod
    def _parts_to_parts_m(cls, parts):
        parts_m = dict()
        for part in parts:
            name = part["name"]
            material = part["material"]
            color = part["color"]
            parts_m[name] = dict(material=material, color=color)
        return parts_m

    @classmethod
    def _normalize_meta(cls, meta):
        meta_d = {}
        meta_l = (
            [
                appier.split_unescape(element, ":", 2)
                if element.startswith("$")
                else appier.split_unescape(element, ":", 1)
                for element in meta
            ]
            if meta
            else []
        )
        for parts in meta_l:
            if len(parts) == 2:
                parts = None, parts[0], parts[1]
            type, key, value = parts
            if key in meta_d:
                old = meta_d[key]
                is_sequence = isinstance(old, (list, tuple))
                if not is_sequence:
                    old = [old]
                old.append(value)
                value = old
            if type == "$list" and not isinstance(value, list):
                value = [value]
            if type == "$int":
                value = int(value)
            if type == "$float":
                value = float(value)
            if type == "$bool":
                value = value in ("1", "true", "True")
            meta_d[key] = value
        return meta_d

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.base_url = appier.conf("RIPE_BASE_URL", RIPE_BASE_URL)
        self.username = appier.conf("RIPE_USERNAME", None)
        self.password = appier.conf("RIPE_PASSWORD", None)
        self.secret_key = appier.conf("RIPE_SECRET_KEY", None)
        self.admin = appier.conf("RIPE_ADMIN", True, cast=bool)
        self.base_url = kwargs.get("base_url", self.base_url)
        self.username = kwargs.get("username", self.username)
        self.password = kwargs.get("password", self.password)
        self.secret_key = kwargs.get("secret_key", self.secret_key)
        self.admin = kwargs.get("admin", self.admin)
        self.session_id = kwargs.get("session_id", None)
        self.token = kwargs.get("token", None)
        self.login_mode = kwargs.get("login_mode", None)

    def build(
        self,
        method,
        url,
        data=None,
        data_j=None,
        data_m=None,
        headers=None,
        params=None,
        mime=None,
        kwargs=None,
    ):
        auth = kwargs.pop("auth", True)
        if auth and self.secret_key:
            headers["X-Secret-Key"] = self.secret_key
        if auth and not self.secret_key:
            params["sid"] = self.get_session_id()

    def get_session_id(self):
        if self.session_id:
            return self.session_id
        if self.login_mode == "pid":
            return self.login_pid()
        return self.login()

    # pylint: disable-next=method-hidden
    def auth_callback(self, params, headers):
        self.session_id = None
        session_id = self.get_session_id()
        params["sid"] = session_id

    def login(self, username=None, password=None, admin=None, token=None):
        self.login_mode = "username"
        username = username or self.username
        password = password or self.password
        admin = admin or self.admin
        token = token or self.token
        if token:
            return self.login_pid(token=token)
        url = self.base_url + ("signin_admin" if admin else "signin")
        contents = self.post(
            url, callback=False, auth=False, username=username, password=password
        )
        self.username = contents.get("username", None)
        self.session_id = contents.get("session_id", None)
        self.tokens = contents.get("tokens", None)
        self.password = password
        self.trigger("auth", contents)
        return self.session_id

    def login_pid(self, token=None):
        self.login_mode = "pid"
        token = token or self.token
        url = self.base_url + "signin_pid"
        contents = self.post(url, callback=False, auth=False, token=token)
        self.username = contents.get("username", None)
        self.session_id = contents.get("session_id", None)
        self.tokens = contents.get("tokens", None)
        self.token = token
        self.trigger("auth", contents)
        return self.session_id

    def is_auth(self):
        if not self.username:
            return False
        if not self.password:
            return False
        return True

    def ping(self):
        url = self.base_url + "ping"
        contents = self.get(url)
        return contents
