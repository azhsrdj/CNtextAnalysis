#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:14:16 2023

@author: wcz
"""

import jieba
import re

def count_keyword_in_lines(lines, keywords):
    keyword_count = {keyword: 0 for keyword in keywords}
    
    for words in lines:
        for word in words:
            if word in keyword_count:
                keyword_count[word] += 1
                
    return keyword_count


def process_file(file_path, stopword_list):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            temp = jieba.lcut(line)
            words = []
            for i in temp:
                i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
                if len(i) > 0 and i not in stopword_list:
                    words.append(i)
            if len(words) > 0:
                lines.append(words)
    return lines

#添加字典
def add_dict():
    f=open("/Users/wcz/Downloads/word2evc/TxTAlysis/ciku.txt","r+",encoding="utf-8")  #百度爬取的字典
    for line in f:
        jieba.suggest_freq(line.rstrip("\n"), True)
    f.close()
 
# 读取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:    # 
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list



if __name__ == "__main__":
    file_path = '/Users/wcz/Downloads/word2evc/TxTAlysis/002230科大讯飞2020年年度报告.txt'  # 将此处替换为你的txt文件路径
    stopword_file = '/Users/wcz/Downloads/word2evc/TxTAlysis/cn_stopwords.txt'
    keywords = ['数字经济', '智能语音', '云计算','大数据']  # 将此处替换为你的关键词列表
    stopword_list = get_stopword_list(stopword_file)
    add_dict()
    Lines = process_file(file_path, stopword_list)
    print(count_keyword_in_lines(Lines, keywords))
