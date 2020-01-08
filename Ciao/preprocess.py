#coding=utf-8

import pandas as pd
import numpy as np
import collections
from sklearn import preprocessing

# userstatistic 列名
# userid
# registering time
# number of reviews
# number of trustors

df_user = pd.read_csv('./dataset/userstatistic.txt',
                      header=None,usecols=[0,2,3],
                      names=['userid','number of reviews','number of trustors'],   #自定义列名
                      sep=r'\:\:\:\:',
                      engine= 'python')
len = df_user.shape[1]
ii =1
for temp in range(1,len):
    df_user.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating user.dat... ")
df_user.to_csv('user.dat', header=None, index=None, sep=':', encoding='utf-8')


# 列名
# UserID
# products
# Categories of the products
# rating
# helpfulness
# time
# content of review
df_rate = pd.read_csv('./dataset/rating.txt',
                      header=None,usecols=[0,1,3],
                      names=['UserID','products','rating'],   #自定义列名
                      sep=r'\:\:\:\:',dtype={'rating':str},
                      engine= 'python')
print("Loading data....")

fea_isnum = df_rate.iloc[:, 2].str.isdigit()
df_rate = df_rate[fea_isnum].copy()

# rate=  df_rate['rating'].unique()
# print(rate)   ['40' '50' '30' '20' '10' '35' '00' '45' '46888593' '25']
df_rate = df_rate[~df_rate['rating'].isin(['46888593'])]
df_rate['rating'] = df_rate['rating'].astype(int)
df_rate['products'] = df_rate['products'].astype(str)

le = preprocessing.LabelEncoder()
df_rate['products'] = le.fit_transform(df_rate['products'].values)

le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
dic_map = pd.DataFrame.from_dict(le_name_mapping,orient='index',columns=['map_record'])
dic_map = dic_map.reset_index().rename(columns = {'index':'id'})

print("Creating mapping ....")
dic_map.insert(1, 'empty', '')
dic_map.to_csv('item_mapping.dat', header=None, index=None, sep=':', encoding='utf-8')

ii =1
len = df_rate.shape[1]
for temp in range(1,len):
    df_rate.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating rating.dat... ")
df_rate.to_csv('rating.dat', header=None, index=None, sep=':', encoding='utf-8')


# Create fake item
df_fake_item = dic_map.iloc[:,2]
df_fake_item= df_fake_item.unique()
df_fake_item = pd.DataFrame(df_fake_item)
len1= df_fake_item.shape[0]
df_rand = pd.DataFrame(np.random.randint(0,2,size=(len1, 1)))
df_fake_item= pd.concat([df_fake_item,df_rand],axis=1)
df_fake_item.insert(1, 'empty', '')
print("Creating fake item.dat... ")
df_fake_item.to_csv('item_fake.dat', header=None, index=None, sep=':')