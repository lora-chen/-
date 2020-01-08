#coding=utf-8

import pandas as pd
import numpy as np
import collections
from sklearn import preprocessing


df_rating = pd.read_csv('./yuanshi/Epinions_rating.txt', sep='\\s+', header=None,
                 names=['item_id','User_id','Rating'],usecols=[0,1,2]
                 )
df_rating = df_rating[['User_id','item_id','Rating']]
len = df_rating.shape[1]
ii =1
for temp in range(1,len):
    df_rating.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating rating.dat... ")
df_rating.to_csv('rating.dat', header=None, index=None, sep=':', encoding='utf-8')





df_user = pd.read_csv('./yuanshi/user_rating.txt', sep='\\s+', header=None,
                 names=['user_id','Trusted_id','Value'],usecols=[0,1,2]
                 )
len = df_user.shape[1]
ii =1
for temp in range(1,len):
    df_user.insert(len-ii, str(ii), '')
    ii=ii+1
print("Creating user.dat... ")
df_user.to_csv('user.dat', header=None, index=None, sep=':', encoding='utf-8')

# Create fake item
df_fake_item = df_rating.iloc[:,2]
df_fake_item= df_fake_item.unique()
df_fake_item = pd.DataFrame(df_fake_item)
len1= df_fake_item.shape[0]
df_rand = pd.DataFrame(np.random.randint(0,2,size=(len1, 1)))
df_fake_item= pd.concat([df_fake_item,df_rand],axis=1)
df_fake_item.insert(1, 'empty', '')
print("Creating fake item.dat... ")
df_fake_item.to_csv('item_fake.dat', header=None, index=None, sep=':')

