#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-05

import json

KEY_TYPE = "type"
KEY_INSIDE = "inside"


class DataConvertor:

    def __init__(self):
        return

    @staticmethod
    def get_raw_objs(source_path):
        raw_objs = []
        with open(source_path, mode="r") as f:
            for line in f:
                try:
                    raw_data_obj = RawDataObj(line)
                    raw_objs.append(raw_data_obj)
                except:
                    continue
        return raw_objs


class RawDataObj:
    def __init__(self, type, inside):
        self.type = type
        self.inside = inside

    def __init__(self, json_str):
        json_obj = json.loads(json_str, strict=False)
        self.type = json_obj.get(KEY_TYPE)
        self.inside = json_obj.get(KEY_INSIDE)

    def get_type(self):
        return self.type

    def get_inside(self):
        return self.inside