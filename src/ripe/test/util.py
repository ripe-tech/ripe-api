#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import ripe


class UtilAPITest(unittest.TestCase):
    def test__query_to_spec(self):
        result = ripe.API._query_to_spec(
            "brand=dummy&model=dummy&locale=en_us&format=webp&initials=AAA&engraving=grey&initials_extra=main:AAA:grey&p=side:leather_dmy:black&p=piping:leather_dmy:black&p=top0_bottom:leather_dmy:black&p=shadow:default:default"
        )
        self.assertEqual(
            result,
            dict(
                brand="dummy",
                model="dummy",
                parts=dict(
                    side=dict(material="leather_dmy", color="black"),
                    piping=dict(material="leather_dmy", color="black"),
                    top0_bottom=dict(material="leather_dmy", color="black"),
                    shadow=dict(material="default", color="default"),
                ),
                initials="AAA",
                engraving="grey",
                initials_extra=dict(main=dict(engraving="grey", initials="AAA")),
            ),
        )

    def test__unpack_query(self):
        result = ripe.API._unpack_query(
            "brand=dummy&model=dummy&p=sole:rubber:red&p=laces:metal:black"
        )
        self.assertEqual(
            result,
            dict(
                brand="dummy", model="dummy", p=["sole:rubber:red", "laces:metal:black"]
            ),
        )

        result = ripe.API._unpack_query(
            "?brand=dummy&model=dummy&p=sole:rubber:red&p=laces:metal:black"
        )
        self.assertEqual(
            result,
            dict(
                brand="dummy", model="dummy", p=["sole:rubber:red", "laces:metal:black"]
            ),
        )

    def test__parse_extra_s(self):
        result = ripe.API._parse_extra_s(["name1:aaa:black", "name2:bbb:white"])
        self.assertEqual(
            result,
            dict(
                name1=dict(initials="aaa", engraving="black"),
                name2=dict(initials="bbb", engraving="white"),
            ),
        )

    def test__tuples_to_parts(self):
        result = ripe.API._tuples_to_parts(
            ["sole:rubber:red", "laces:metal:black", "side:rubber:white"]
        )
        self.assertEqual(
            result,
            [
                dict(name="sole", material="rubber", color="red"),
                dict(name="laces", material="metal", color="black"),
                dict(name="side", material="rubber", color="white"),
            ],
        )

    def test__parts_to_parts_m(self):
        result = ripe.API._parts_to_parts_m(
            [
                dict(name="sole", material="rubber", color="red"),
                dict(name="laces", material="metal", color="black"),
                dict(name="side", material="rubber", color="white"),
            ]
        )
        self.assertEqual(
            result,
            dict(
                sole=dict(material="rubber", color="red"),
                laces=dict(material="metal", color="black"),
                side=dict(material="rubber", color="white"),
            ),
        )
