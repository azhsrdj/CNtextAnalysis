# DataMerge
县域 企业 行业 数据匹配和合并

## 前言

用一个案例代码，来展示这个这个合并怎么完成

## 需求描述

有如下三个表格

表1包含了县名CountryName、行政编码CountryCode、行业分类F1-F6。设置行业分类的目的是通过县域与部分企业建立了关联，而这些企业又分属不同的行业，我的最终需求是获得一份县与企业关联，以及县通过企业与县发生关联的数据。

表2包含了所有企业的名称以及所属的行业，其中CompanyName代表企业名称，CompanyCode代表企业代码，一般为6位数，行业分类F1-F6同上。

表X1_old是一份试例数据，其格式与CNtextAnalysis处理后生成的文本结果基本一致，文件名“表X1_old” 表示这是企业X1的县域关联数据表。CountryName同表1，表示县名，Treat表示与县关联，数字从1到N不等。

我的需求是将表2和表X1_old的数据合入表1，最后通过遍历所有企业数据，将X1～Xn的所有企业合入表1



## 设计思路



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

