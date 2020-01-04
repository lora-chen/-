from pandas import Series,DataFrame
import pandas as pd

data = {'12':['33'],
       '22':['"1103";"kuala lumpur, \"n/a\", malaysia";NULL']}
df = DataFrame(data)
df.str.replace("\\\"n/a\\\"","n/a",inplace=True)
print(df)

srt= '\\\"n/a\\\"'
print (srt)
a= srt.replace(srt,"n/a")
print(a)