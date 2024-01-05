# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import os
import pdfplumber


def pdf_to_txt(input_path, output_path):
    """
    将一个目录内的PDF文件批量转换为txt文件

    Parameters:
        input_path (str): 输入目录的路径，其中包含PDF文件
        output_path (str): 输出目录的路径，用于保存转换后的txt文件
    """
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    # 遍历输入目录内的文件
    for filename in os.listdir(input_path):
        if filename.endswith(".pdf"):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, filename.replace(".pdf", ".txt"))

            # 使用pdfplumber打开PDF文件并提取文本内容
            with pdfplumber.open(input_file) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text()

            # 将文本内容保存到txt文件
            with open(output_file, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)

if __name__ == "__main__":
    # 输入目录和输出目录的路径
    input_directory = "/Volumes/Charles/数字经济 /技术经济小论文/未命名文件夹/"
    output_directory = "/Volumes/Charles/数字经济 /技术经济小论文/未命名文件夹/"


    pdf_to_txt(input_directory, output_directory)
