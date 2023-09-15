#!/usr/bin/env python
# coding=utf-8
# Author: Cong
# Date: 2023-09-14
import os.path

from pdf2image import convert_from_path
from cnocr import CnOcr


def pdf_to_images(pdf_file, output_path, **kwargs):
    images = convert_from_path(pdf_file, last_page=5)
    #if not os.path.exists(output_path):
    #    os.makedirs(output_path)
    os.makedirs(output_path)
    for i, image in enumerate(images):
        image.save(f"{output_path}/page_{i + 1}.png", "PNG")
    return len(images)


def images_to_txt(image_path, output_file, images_num, **kwargs):
    with open(output_file, "w") as f:
        ocr = CnOcr()
        pages = images_num  # 上一步有多少页，这里就是多少

        for idx in range(pages):
            name = f'{image_path}/page_' + str(idx + 1) + '.png'
            res = ocr.ocr(name)
            string_list = []
            for item in res:
                string_list.append(item.get("text"))
            ocr_result_string = "\n".join(string_list)
            f.write(ocr_result_string)


if __name__ == "__main__":
    pages_num = pdf_to_images("/Users/hanting.cong/Desktop/毁伤数据集/大模型/07-兵器学会/论文（正文）1.pdf", "/Users/hanting.cong/Desktop/毁伤数据集/大模型/07-兵器学会/论文（正文）1 Images")
    images_to_txt("/Users/hanting.cong/Desktop/毁伤数据集/大模型/07-兵器学会/论文（正文）1 Images", "/Users/hanting.cong/Desktop/毁伤数据集/大模型/07-兵器学会/论文（正文）1.txt", pages_num)