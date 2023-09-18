#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-18
import json
import os

folder_path = "/path/to/your/folder"

data_types = []

for root, directories, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        print(file_path)
        with open(file_path, "r") as f:
            items = json.load(f)
            for item in items:
                data_types.append(item['dataType'])

print(list(set(data_types)))