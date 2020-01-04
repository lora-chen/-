#coding=utf-8

import pandas as pd
import numpy as np
import collections

"""
BX-Users.csv 要先用excel把“n/a”替换成“ ”,直接用这个BX-Users_modified.csv
或者读取时用
# df0 = pd.read_csv('./yuanshi/BX-Users.csv',header=0,sep=';',engine= 'python',encoding='latin-1', error_bad_lines = False)
"""

"已经用excel先把“\"n/a\"”替换成" "    "
df_0 = pd.read_csv('./yuanshi/BX-Users_modified.csv',usecols=[0,1,2,3], names=['UserID','Location','Country','Age'],
                      sep=',',
                      engine= 'python',
                      encoding='latin-1',
                   )
df_0 = df_0.drop([0])
print("Loading data....")
df_0 = df_0.fillna(-1)
ii=1
len = df_0.shape[1]
for temp in range(1,len):
    df_0.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating user.dat... ")
df_0.to_csv('user.dat', header=None, index=None, sep=':', encoding='utf-8')


df = pd.read_csv('./yuanshi/BX-Book-Ratings_modified.csv',
                      header=0,
                      sep=',',
                      engine= 'python')
dict_replace = {'\"':'' }
df.replace(dict_replace,inplace=True)
ii=1
len = df.shape[1]
for temp in range(1,len):
    df.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating rating.dat... ")
df.to_csv('rating.dat', header=None, index=None, sep=':')


df = pd.read_csv('./yuanshi/BX-Books_modified.csv',usecols=[0,2,3,4],
                      header=0,
                      sep=',',
                      engine= 'python')
print(df.shape[1])
print(df.head())
ii=1
len = df.shape[1]
for temp in range(1,len):
    df.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating item.dat... ")
df.to_csv('item.dat', header=None, index=None, sep=':')


