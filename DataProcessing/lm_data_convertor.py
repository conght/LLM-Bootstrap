#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-05

import json
from data_convertor import DataConvertor, RawDataObj


class LMDataConvertor(DataConvertor):
    def __int__(self):
        return

    def convert_to_text_only(self, src_path, dst_path):
        lm_data_instances = []
        raw_data_objs = self.get_raw_objs(src_path)
        for raw_data_obj in raw_data_objs:
            lm_text_only_obj = {"text": raw_data_obj.get_inside()}
            lm_data_instances.append(lm_text_only_obj)

        #with open(dst_path, mode="w", encoding="utf8") as f:
        #    f.write(json.dumps(LMDataSet("text_only", lm_data_instances).to_json(), ensure_ascii=False))
        print(LMDataSet("text_only", lm_data_instances).to_json())


class LMDataSet:
    def __init__(self, data_type, instances):
        self.type = data_type
        self.instances = instances

    def to_json(self):
        data = {
            "type": self.type,
            "instances": list(self.instances)
        }
        return json.dumps(data, ensure_ascii=False)


