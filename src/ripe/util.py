#!/usr/bin/python
# -*- coding: utf-8 -*-

import appier


class UtilAPI(object):
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
