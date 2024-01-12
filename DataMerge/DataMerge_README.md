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



## 文件

example_debug.py

------

## 正式的文件

 [example_debug_new.py](example_debug_new.py) ： 生成可用的县域和企业帮扶联系的面板的程序

 [CountryName.csv](CountryName.csv) ， [CountryName_AllCHN.csv](CountryName_AllCHN.csv)  分别是西部6省县和全国县市的名单 对照于表1

 [Industry.csv](Industry.csv)  是2021年底，4000多家上市公司的名单，包含所属行业的信息，对照于表2

 [Country_Company_relationship.xlsx](Country_Company_relationship.xlsx)  是程序执行后，最终的面板文件，本文件以2021年为例。



