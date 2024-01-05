#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:14:16 2023

@author: wcz
"""

import jieba
import re
import jieba
import re
import numpy as np
from sklearn.decomposition import PCA
import gensim
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import matplotlib
import glob
import os



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

def process_file(file_path, stopword_list):
   
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            temp = jieba.lcut_for_search(line)
            words = []
            for i in temp:
                i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
                if len(i) > 0 and i not in stopword_list:
                    words.append(i)
            if len(words) > 0:
                lines.append(words)
    return lines

# %% 读取训练文件
f = open("/Users/wcz/Downloads/信通院文档-文本分析/中国数字经济发展白皮书（2017年）.txt", 'r',encoding='utf-8') #读入文本
stopword_file = '/Users/wcz/Downloads/word2evc/TxTAlysis/cn_stopwords.txt'#停用词路径
stopword_list = get_stopword_list(stopword_file)
add_dict()
lines = []
for line in f: #分别对每段分词
    temp = jieba.lcut(line)  #结巴分词 精确模式
    words = []
    for i in temp:
        #过滤掉所有的标点符号
        i = re.sub("[\s+\.\!\/_,$%^*(+\"\'””《》]+|[+——！，。？、~@#￥%……&*（）：；‘]+", "", i)
        if len(i) > 0 and i not in stopword_list:
            words.append(i)
    if len(words) > 0:
        lines.append(words)
print(lines[0:5])#预览前5行分词结果
lines.extend(lines)

#%% 训练模型


# 调用Word2Vec训练
# 参数：size: 词向量维度；window: 上下文的宽度，min_count为考虑计算的单词的最低词频阈值
def GenModel(lines):
    model = Word2Vec(lines,vector_size = 20, window = 10 , min_count = 1, epochs=10, negative=10,sg=0)
    return model
# sg=0 是CBOW 1是skip-gram



def TrainModel(model, keywords):

    # print("数据的词向量：\n",model.wv.get_vector('数据'))
    # print("\n和数据相关性最高的前20个词语：")
    #    model.wv.most_similar('数字经济', topn = 20)# 与孔明最相关的前20个词语
    similar_words = []
    for keyword in keywords:
        if keyword in model.wv:
            top_10_similar_words = model.wv.most_similar(keyword, topn=20)
            similar_words.extend([word for word, similarity in top_10_similar_words])
    similar_words = list(set(similar_words))
    return similar_words

#%% 读取训练文件+训练模型

Trainfiles = glob.glob('/Users/wcz/Downloads/信通院文档-文本分析/filedir/*.txt')
stopword_file = '/Users/wcz/Downloads/word2evc/TxTAlysis/cn_stopwords.txt'#停用词路径
stopword_list = get_stopword_list(stopword_file)
add_dict()
Lines = []
for file_path in Trainfiles:
    lines = process_file(file_path, stopword_list)
    Lines.extend(lines)
# keywords = ['数字经济', '大数据', '云计算','智能','智慧']
keywords = []
with open("/Users/wcz/Downloads/word2evc/TxTAlysis/ciku.txt", "r", encoding="utf-8") as f:
    for line in f:
        keywords.append(line.strip())
model = GenModel(Lines)
print(TrainModel(model, keywords))
# similar_words = []
# for keyword in keywords:
#     if keyword in model.wv:
#         top_10_similar_words = model.wv.most_similar(keyword, topn=50)
#         similar_words.extend([word for word, similarity in top_10_similar_words])
# similar_words = list(set(similar_words))
# print(similar_words)

