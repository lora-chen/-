from pandas import Series,DataFrame
import pandas as pd
import numpy as np


df_user = pd.read_csv('user.dat',
                      header=None,
                      engine= 'python')
df_user= df_user[0:20]
df_user.to_csv('user_sample.dat', header=None, index=None, encoding='utf-8')

df_item = pd.read_csv('item_fake_BX.dat',
                      header=None,
                      engine= 'python')
df_item= df_item[0:20]
df_item.to_csv('item_sample_fake_BX.dat', header=None, index=None, encoding='utf-8')

df_rate = pd.read_csv('rating.dat',
                      header=None,
                      engine= 'python')
df_rate= df_rate[0:20]
df_rate.to_csv('rating_sample.dat', header=None, index=None, encoding='utf-8')