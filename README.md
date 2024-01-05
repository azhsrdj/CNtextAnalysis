# CNtextAnalysis
对中文txt文本进行关键词词频统计

## 前言

本文旨在对之前写的为分析上市公司年报关键词词频统计的代码进行记录。

## 需求描述

## 设计思路
![](https://github.com/azhsrdj/CNtextAnalysis/blob/main/%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90%E4%BB%A3%E7%A0%81%E6%B5%81%E7%A8%8B%E5%9B%BE.drawio.png)

## 文件准备

本项目重要的文件有如下几个：

1. ciku.txt 记录所要统计的关键词，程序需要用到这个文件两次，第一次是将其添加进jieba分词的基础词库，因为有些关键词可能不在jieba的基础词库中，第二次是在keyword_count时用来统计文本中关键词出现的次数。
2. cn_stopwords.txt 记录了分词时需要停用的停用词。

本项目需要根据实际情况修改源代码的地方：

由于读取源文件和输出目录被代码写死，在不同计算机下使用本项目需要修改源文件目录和输出文件目录：

main下

```python
files = glob.glob('/Users/wcz/Downloads/B2021txt/*.txt') 
```

记录了源文件目录，这里的txt文档是pdf2txt转化将pdf年报文档转化成的txt文档。

```python
output_csv = '/Users/wcz/Downloads/C2021txt/' + os.path.splitext(os.path.basename(file_path))[0] + '.csv' 
```

记录了输出文件目录和输出文件的命名规则，转化后是一份csv文档。包含 Keyword，Count  两列，最后一行记录Total

```python
with open('/Users/wcz/Downloads/word2evc/TxTAlysis/ciku.txt', 'r', encoding='utf-8') as f:
        keywords = [line.strip() for line in f]
```

这行代码

```python
stopword_file = '/Users/wcz/Downloads/word2evc/TxTAlysis/cn_stopwords.txt'
```

记录了停用词目录


