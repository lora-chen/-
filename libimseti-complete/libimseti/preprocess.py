#coding=utf-8

import pandas as pd
import numpy as np
import collections


df0 = pd.read_csv('./yuanshi/gender.dat',
                      header=None,
                      names=['UserID','Gender'],   #自定义列名
                      sep=',',
                      engine= 'python')
print("Loading data....")
df0.insert(1, 'empty', '')
print("Creating user.dat... ")
df0.to_csv('user.dat', header=None, index=None, sep=':', encoding='utf-8')

df = pd.read_csv('./yuanshi/ratings.dat',
                      header=None,
                      names=['UserID','ItemID','Score'],   #自定义列名
                      sep=',',
                      engine= 'python')
df.insert(2, 'empty', '')
df.insert(1, 'empty1', '')
print("Creating rating.dat... ")
df.to_csv('rating.dat', header=None, index=None, sep=':', encoding='utf-8')

df3 = df['ItemID'].unique()
df3 = pd.DataFrame(df3)
df3.insert(1, 'Gender', df3)
dict1 = collections.OrderedDict()
arrary_UserID = df0['UserID'].values
arrary_Gender = df0['Gender'].values
for ii in range(len(arrary_UserID)):
    dict1[arrary_UserID[ii]] = arrary_Gender[ii]

df3['Gender'].replace(dict1,inplace=True)
df3.insert(1, 'empty', '')
print("Creating item.dat... ")
df3.to_csv('item.dat', header=None, index=None, sep=':', encoding='utf-8')
