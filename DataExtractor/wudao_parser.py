#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-18
import json
import os


def cal_distribution(total_size):
    data = [
        (173, "博客"),
        (65, "豆瓣话题"),
        (40, "百科"),
        (26, "孕育常识"),
        (7, "资讯"),
        (7, "新闻"),
        (6, "科技"),
        (6, "小红书攻略"),
        (6, "娱乐"),
        (5, "农业"),
        (3, "国际"),
        (3, "医学问答"),
        (2, "社会"),
        (2, "汽车"),
        (2, "旅行"),
        (2, "文化"),
        (2, "房产"),
        (2, "体育"),
        (1, "经验"),
        (1, "经济"),
        (1, "科普文章"),
        (1, "百家号文章"),
        (1, "游戏"),
        (1, "法律"),
        (1, "教育")
    ]

    job_config = {}
    for count, datatype in data:
        percentage = (count / sum(c for c, _ in data)) * 100
        size = int(total_size * percentage)
        job_config[datatype] = {'size': size, 'percentage': percentage}

    return job_config


def sample_wudao_corpus(folder_path, output_file, job_config):
    with open(output_file, "w") as output:
        for root, directories, files in os.walk(folder_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                print(file_path)
                with open(file_path, "r") as f:
                    items = json.load(f)
                    for item in items:
                        data_types = item['dataType']
                        if data_types not in job_config.keys():
                            continue
                        content = item['content']
                        content_len = len(content) * 2.5
                        job_config[data_types]['size'] = job_config[data_types]['size'] - content_len
                        if job_config[data_types]['size'] < 0:
                            job_config.pop(data_types)
                        output.write(json.dumps({"type": "text", "inside": content}, ensure_ascii=False) + '\n')




if __name__ == "__main__":
    job_config = cal_distribution( 25 * 1024 * 1024)
    sample_wudao_corpus("test/", "test_result.jsonl", job_config)

