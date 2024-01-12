#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:41:30 2024

@author: wcz
"""

import pandas as pd
import os 
import re
import glob

#%% 读取表格
df2 = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CompanyName.csv',dtype={'CompanyCode': str})
for index,  row in df2.iterrows():
    df2.loc[index,df2['IndustryCode'][index]] = 1
    
# df_tableX1old = pd.read_csv('/Users/wcz/Downloads/表X1_old.csv')
# df1 = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CountryName.csv') 只计算西部6省的
df1 = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CountryName_AllCHN_1.csv')
df1.iloc[:,3:]=0 # 初始化，所有行业的联系都是0


#%% 针对表X1_old的处理
files = glob.glob('/Users/wcz/Downloads/C2021txt/*.csv') 
# 读取/Users/wcz/Downloads/C2021txt/下所有的csv文件，开始遍历，将数据合并进表1中
for file_path in files:
    file_name = os.path.basename(file_path)
    CompanyCode = re.search(r"\d{6}", file_name).group()
    df_treat = pd.read_csv(file_path)
    df_treat.rename(columns={'Keyword':'CountryName'},inplace = True)
    df_CountryCode = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CountryName_AllCHN_1.csv')
    df_treat = pd.merge(df_treat, df_CountryCode, how='left', on=['CountryName'])
    
# =============================================================================
#     这里要加一段代码，将CountryCode合并入 df_treat 中，因为原来的csv文件，只有CountryName 没有CountryCode
#     
# =============================================================================
    df2_clear  = df2.drop(df2[df2['CompanyCode']!=CompanyCode].index) # 将企业“X1”保留，其他行删除
    if df_treat.Count.loc[df_treat[df_treat.CountryName == 'Total'].index.tolist()[0] ] == 0:
        continue
    df_treat = df_treat.loc[df_treat['Count'] != 0]
    df_treat = df_treat.drop(df_treat.index[-1])# df_treat中Count为0的行删除，并删除Total项
    df2_clear = df2_clear.append([df2_clear]*(df_treat.shape[0]-1)) # df2的行数与 df_treat 对齐
    df_treat = df_treat.reset_index(drop=True) 
    df2_clear = df2_clear.reset_index(drop=True)
    # 重新index
    df_treat = pd.concat([df_treat.iloc[:,0:4],df2_clear.iloc[:,4:]],axis=1)
    # df2 的行业表单拼接到 df_tableX1old_clear 中
    CountryCode = df_treat['CountryCode'].T.tolist() # 获得df_treat中包含的CountryCode，下面要用到
# =============================================================================
#     分界线 以下是数据合并到表1
# =============================================================================
    temp = df1.loc[df1['CountryCode'].isin(CountryCode)] 
    df1 = df1.drop(temp.index,axis=0) 
    # 剪切，提去“CountryName” 变量中的行

    temp2 = temp.iloc[:,3:] # 切数据，只保留行业
    x = temp2.index.to_series()
    x = pd.DataFrame(x).reset_index(drop=True)
    df_treat = pd.concat([df_treat,x],axis=1)

    df_treat = df_treat.set_index(0)

    temp2 = temp2.add(df_treat.iloc[:,3:],fill_value=0)

    temp = pd.concat([temp.iloc[:,0:2],temp2],axis=1)

    df1 = pd.concat([df1,temp],axis=0)

    df1.sort_index(inplace=True)

    # 用一个特殊技巧合并
#%% 生成文件


with pd.ExcelWriter('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/Country_Company_relationship.xlsx') as writer:
    df1.to_excel(writer, sheet_name='sheet1')
    

