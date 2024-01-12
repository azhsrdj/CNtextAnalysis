#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:41:30 2024

@author: wcz
"""

import pandas as pd
import os 
import re

#%% 读取表格
df2 = pd.read_csv('/Users/wcz/Downloads/表2.csv')
df_tableX1old = pd.read_csv('/Users/wcz/Downloads/表X1_old.csv')
df1 = pd.read_csv('/Users/wcz/Downloads/表1.csv')
df1.iloc[:,2:]=0 # 初始化，所有行业的联系都是0


#%% 针对表X1_old的处理
df2_clear  = df2.drop(df2[df2['CompanyName']!='X1'].index) # 将企业“X1”保留，其他行删除
df_tableX1old_clear = df_tableX1old.dropna(axis=0,how='any',subset=['Treat']) # tableX1中Treat为0的行删除
df2_clear = df2_clear.append([df2_clear]*(df_tableX1old_clear.shape[0]-1)) # df2的行数与df_tableX1old_clear 对齐
df_tableX1old_clear = df_tableX1old_clear.reset_index(drop=True) 
df2_clear = df2_clear.reset_index(drop=True)
# 重新index
df_tableX1old_clear = pd.concat([df_tableX1old_clear,df2_clear.iloc[:,2:]],axis=1)
# df2 的行业表单拼接到 df_tableX1old_clear 中
CountryName = df_tableX1old_clear['CountryName'].T.tolist() # 获得df_tableX1old_clear中包含的CountryName，下面要用到

#%%  df_tableX1old_clear 合并到表1

 # 

temp = df1.loc[df1['CountryName'].isin(CountryName)] 
df1 = df1.drop(temp.index,axis=0) 
# 剪切，提去“CountryName” 变量中的行

temp2 = temp.iloc[:,2:] # 切数据，只保留行业
x = temp2.index.to_series()
x = pd.DataFrame(x).reset_index(drop=True)
df_tableX1old_clear = pd.concat([df_tableX1old_clear,x],axis=1)

df_tableX1old_clear = df_tableX1old_clear.set_index(0)

temp2 = temp2.add(df_tableX1old_clear.iloc[:,2:],fill_value=0)

temp = pd.concat([temp.iloc[:,0:2],temp2],axis=1)

df1 = pd.concat([df1,temp],axis=0)

df1.sort_index(inplace=True)

# 用一个特殊技巧合并
#%%


# Full path string
full_path = "/Users/wcz/Downloads/C2021txt/000002.SZ-万科A-万科A：2021年年度报告-20220331.csv"

# Extract the file name
file_name = os.path.basename(full_path)

print(file_name)