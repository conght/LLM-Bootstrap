#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-15


'''
Requirements
1. 把被断掉的句子拼起来
2. 大标题和作者信息去掉 // DONE
3. 摘要删掉 // DONE
4. 关键词删掉 // DONE
5. 标题标号删掉  // DONE
    - 1相关术语
    - 2.1弹药战斗部威力
    - 2. 2目标易损性评估
    - 3. 2. 1制定作战火力计划、有效控制战争进程的重要依据
6. 标号删掉
    - （1）
7. 页眉删掉 // DONE
    - .6毁伤评估技术的概念、内涵及其作用意义<
8. 参考文献 // DONE
    - 重大作用。
    - 参考文献
    - [1」王凤英，刘天生·毁伤理论与技术〔M」、北京：北京理工大学出版社，2009
    -[2〕王儒策，赵国志，杨绍卿，弹药工程〔M].北京：北京理工大学出版社，2001
9. 表2 / 图1 // DONE
'''

import re


def remove_reference(lines, dry_run=False):
    '''
    删除文章末尾的参考文献
    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    states = 0
    for line in lines:
        line = line.strip()
        if line == "参考文献":
            targeted_lines.append(line)
            states = states + 1
        elif line == "作者简介":
            result_lines.append(line)
            states = states - 1
        elif states > 0:
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print(targeted_lines)
    if dry_run:
        print(result_lines)
        result_lines = None

    return result_lines, targeted_lines


def remove_author_brief(lines, dry_run=False):
    '''
    删除文章末尾的作者简介
    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    states = 0
    for line in lines:
        line = line.strip()
        if line == "作者简介":
            targeted_lines.append(line)
            states = states + 1
        elif states > 0:
            targeted_lines.append(line)
            states = states - 1
        else:
            result_lines.append(line)

    print(targeted_lines)
    if dry_run:
        print(result_lines)
        result_lines = None

    return result_lines, targeted_lines


def remove_abstract(lines, dry_run=False):
    '''
    删除摘要和关键字
    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    states = 0
    for line in lines:
        line = line.strip()
        if line.startswith("作者简介"):
            targeted_lines.append(line)
            states = states + 1
        elif line.startswith("关键词"):
            targeted_lines.append(line)
            states = states - 1
        elif states > 0:
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


def remove_abstract2(lines, dry_run=False):
    '''
    删除摘要和关键字
    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    states = 0
    for line in lines:
        line = line.strip()
        if "摘要" in line:
            targeted_lines.append(line)
            states = states + 1
        elif line.startswith("关键词"):
            targeted_lines.append(line)
            states = states - 1
        elif states > 0:
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


def remove_authors(lines, dry_run=False):
    '''
    删除文章开头的作者信息
    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    states = 0
    for line in lines:
        line = line.strip()
        if line.startswith("(1."):
            targeted_lines.append(line)
            states = states + 1
        elif line.startswith("摘要"):
            result_lines.append(line)
            states = states - 1
        elif states > 0:
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


def remove_footer(lines, dry_run=False):
    '''

    :param lines:
    :return:
    '''
    targeted_lines = []
    result_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("·"):
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


def remove_label(lines, dry_run=False):
    '''

    :param lines:
    :param dry_run:
    :return:
    '''
    #pattern = r'^(\d+(\.\d+)*|\.\d+)$'
    pattern = r'^(?:\d+(\.\d+)*|\.\d+).*'
    targeted_lines = []
    result_lines = []

    for line in lines:
        origal_line = line
        line = line.strip()
        if re.match(pattern, line):
            targeted_lines.append(origal_line)
        else:
            result_lines.append(origal_line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


def remove_fig_label(lines, dry_run=False):
    '''

        :param lines:
        :param dry_run:
        :return:
        '''
    #pattern = r'^(图|表)\d+$'
    pattern = r'^(图|表)\d+.*'
    targeted_lines = []
    result_lines = []

    for line in lines:
        line = line.strip()
        if re.match(pattern, line):
            targeted_lines.append(line)
        else:
            result_lines.append(line)

    print("删除目标：\n" + "\n".join(targeted_lines))
    if dry_run:
        print("保留目标：\n" + "\n".join(result_lines))
        result_lines = None

    return result_lines, targeted_lines


if __name__ == "__main__":
    test = [
        "重大作用。",
    "参考文献",
    "[1」王凤英，刘天生·毁伤理论与技术〔M」、北京：北京理工大学出版社，2009",
    "[2〕王儒策，赵国志，杨绍卿，弹药工程〔M].北京：北京理工大学出版社，2001",
   " [3]",
    "作者简介",
    "范开军（1963一），男，研究员级高级工程师。",
    "关键词：兵器科学与技术；毁伤；毁伤评估；概念体系"]

    test2 = [
        "实弹演习中，靶标设计与靶场建设、弹药分配及毁伤效果预测、实弹毁伤效果数据获取、演习效果评",
        "摘要：有效获取和评价实弹演习中武器弹药毁伤效果，对科学评判演习效果、提出相关优化和改进",
    "关键词：实弹演习；毁伤评估；毁伤预估；毁伤测试"
    ]
    #remove_reference(test, dry_run=True)
    #remove_abstract(test2, dry_run=True)
    #remove_label()
    #remove_fig_label()

    '''
    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/论文（正文）3.txt'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/论文（正文）3 cleaned.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines, t1 = remove_reference(lines)
        lines, t2 = remove_abstract(lines)
        lines, t3 = remove_label(lines)
        lines, t4 = remove_fig_label(lines)
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        with open(output_file_path, 'w') as file:
            file.write("\n".join(lines))

  
    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/论文（正文）3 cleaned.txt'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/论文（正文）3 final.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = "".join(lines).replace('\n', '').split("。")
        print(lines)
        with open(output_file_path, 'w') as file:
            for line in lines:
                file.write('{"type":"text", "inside":"'+ line + '。"}\n')


    

    import json


    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/reult_book_包含弹药学和弹药实验技术.json'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/uncleaned/reult_book_包含弹药学和弹药实验技术.txt'
    with open(file_path, 'r') as file:
        data = json.load(file)
        lines = []
        for item in data:
            for line in item['content_split_list']:
                lines.append(line)
        with open(output_file_path, 'w') as file:
            for line in lines:
                pattern = r'^(?:\d+(\.\d+)*|\.\d+).*'
                line = line.strip()
                if re.match(pattern, line):
                    continue
                file.write('{"type":"text", "inside":"' + line + '。"}\n')
   

    #cat 20230915_raw.jsonl | awk - F'"inside":"' '{print $2}' | awk - F'"}' '{print $1}' > 20230915_raw.txt

    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/20230915_raw.txt'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/20230915_raw.jsonl'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines, t2 = remove_abstract2(lines)
        lines, t3 = remove_label(lines)
        lines, t4 = remove_fig_label(lines)
        print(t1)
        print(t2)
        print(t3)
        print(t4)
        with open(output_file_path, 'w') as file:
            file.write("\n".join(lines))
   

    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/论文raw/1-4_paper.txt'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/论文raw/1-4_paper_cleaned.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines, t1 = remove_footer(lines)
        print(len(t1))
    with open(output_file_path, 'w') as file:
        file.write("\n".join(lines))
    

    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/论文raw/1-4_paper_cleaned.txt'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/论文raw/1-4_paper_final.txt'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = "".join(lines).replace('\n', '').split("。")
        print(lines)
        with open(output_file_path, 'w') as file:
            for line in lines:
                file.write('{"type":"text", "inside":"' + line + '。"}\n')
    '''
    file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/20230915_raw.jsonl'
    output_file_path = '/Users/hanting.cong/Desktop/毁伤数据集/v2023.09.15/20230915.jsonl'
    with open(file_path, 'r') as file:
        lines = file.readlines()
        results = []
        for line in lines:
            if "如图" in line:
                continue
            if "如表" in line:
                continue
            if "所示" in line:
                continue
            results.append(line)

        with open(output_file_path, 'w') as file:
            file.write("".join(results))
