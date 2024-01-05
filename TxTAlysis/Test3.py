#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 14:09:32 2023

@author: wcz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:14:16 2023

@author: wcz
"""

import os
import glob
import jieba
import re
import pandas as pd

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
    
    files = glob.glob('/Users/wcz/Downloads/A2019txt/*.txt')
    stopword_file = '/Users/wcz/Downloads/word2evc/TxTAlysis/cn_stopwords.txt'
    
    stopword_list = get_stopword_list(stopword_file)
    add_dict()
    with open('/Users/wcz/Downloads/word2evc/TxTAlysis/ciku.txt', 'r', encoding='utf-8') as f:
        keywords = [line.strip() for line in f]
    for file_path in files:
        if os.path.basename(file_path) == '/Users/wcz/Downloads/word2evc/TxTAlysis/ciku.txt':  # Skip keywords.txt file
            continue
        lines = process_file(file_path, stopword_list)
        keyword_count = count_keyword_in_lines(lines, keywords)
        df = pd.DataFrame(list(keyword_count.items()), columns=['Keyword', 'Count'])
        output_csv = '/Users/wcz/Downloads/B2019txt/' + os.path.splitext(os.path.basename(file_path))[0] + '.csv'
        df.to_csv(output_csv, index=False, encoding='utf_8_sig')
        
        
