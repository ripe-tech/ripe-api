#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier

import ripe

def get_api():
    return ripe.Api(
        username = appier.conf("RIPE_USERNAME"),
        password = appier.conf("RIPE_PASSWORD")
    )
