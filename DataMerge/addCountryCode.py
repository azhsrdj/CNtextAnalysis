#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:03:05 2024

@author: wcz
"""

import pandas as pd

df1 = pd.read_csv('/Users/wcz/Downloads/word2evc/TxTAlysis/country_name.txt', names = ['CountryName'])

df2 = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CountryName.csv')

df1 = pd.merge(df1, df2, how='left', on=['CountryName'])




# =============================================================================
# 
# =============================================================================
df1 = pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CompanyName.csv')

df1['CompanyCode'] = df1['CompanyCode'].astype(str).apply(lambda x: x.zfill(6))

df1['IndustryCode'], df1['Province'] = df1['Province'], df1['IndustryCode']

df1.to_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/tt.csv', index=False, encoding='utf-8')



df1.rename(columns={'CountryName':'a'})
df1.rena


#%%


df = pd.read_csv('/Users/wcz/Downloads/C2021txt/002298.SZ-中电兴发-中电兴发：2021年年度报告-20220428.csv')
df = df.loc[df['Count'] != 0]
df = df.drop(df.index[-1])
#%%


df =  pd.read_csv('/Users/wcz/Downloads/CNtextAnalysis/DataMerge/CompanyName.csv')
