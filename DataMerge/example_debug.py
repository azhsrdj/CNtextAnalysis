#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 21:41:30 2024

@author: wcz
"""

import numpy as np
import pandas as pd
from numpy import *

df2 = pd.read_csv('/Users/wcz/Downloads/表2.csv')
df_tableX1old = pd.read_csv('/Users/wcz/Downloads/表X1_old.csv')

# t = df2.columns[2:].tolist()
# for col in t:
#     df_tableX1old[col] = pd.NA  

df2_clear  = df2.drop(df2[df2['CompanyName']!='X1'].index)
df_tableX1old_clear = df_tableX1old.dropna(axis=0,how='any',subset=['Treat'])
df2_clear = df2_clear.append([df2_clear]*(df_tableX1old_clear.shape[0]-1))
df_tableX1old_clear = df_tableX1old_clear.reset_index(drop=True)
df2_clear = df2_clear.reset_index(drop=True)
df_tableX1old_clear = pd.concat([df_tableX1old_clear,df2_clear.iloc[:,2:]],axis=1)
print(df_tableX1old_clear)

CountryName = df_tableX1old_clear['CountryName'].T.tolist()

# =============================================================================
# 分界线
# =============================================================================
df1 = pd.read_csv('/Users/wcz/Downloads/表1.csv')

df1.iloc[:,2:]=0

temp = df1.loc[df1['CountryName'].isin(CountryName)]

df1 = df1.drop(temp.index,axis=0)

temp2 = temp.iloc[:,2:]
x = temp2.index.to_series()
x = pd.DataFrame(x).reset_index(drop=True)
df_tableX1old_clear = pd.concat([df_tableX1old_clear,x],axis=1)

df_tableX1old_clear = df_tableX1old_clear.set_index(0)

temp2 = temp2.add(df_tableX1old_clear.iloc[:,2:],fill_value=0)

temp = pd.concat([temp.iloc[:,0:2],temp2],axis=1)


df1 = pd.concat([df1,temp],axis=0)
print(temp2.index)

df1.sort_index(inplace=True)
