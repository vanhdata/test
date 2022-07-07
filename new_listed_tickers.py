#  import libs 
from cmath import e
import re
from bs4 import BeautifulSoup
import selenium
import numpy
import requests
import pandas as pd
import numpy as np
import sqlalchemy
import json

from delisted_tickers import DATASET


# having API, get API (json form)
# 2 - New Listed tickers

new_listed_url = ("https://www.hsx.vn/Modules/Listed/Web/NewSymbolList?_search=false&"
    "nd=1656993119507&rows=30&page=1&sidx=id&sord=desc")

request_url = requests.get(new_listed_url)
print(request_url) # response 200 is ok
result = request_url.json()
print(result['rows'])
data = result['rows']
print(data[1])
print(len(data)) # 9

DATASET = []
for a in range(int(result['total'])):
    dataset =[]
    for i in range(len(data)):
        record = data[i]
        cell_record = record['cell']
        dataset.append(cell_record)
# print(pd.DataFrame(dataset))
*DATASET, = dataset

print(pd.DataFrame(dataset).iloc[:,0])
print(pd.DataFrame(DATASET))
print('-------------------')
dataset2 = pd.DataFrame(DATASET, columns=['id','stt','tickers','isin','figi','company_name','address','regist_date','regist_volume'])
# change datatype from object to fit in columns
    # dataset2.astype({0:'int32'}).dtypes
dataset2.info()
# dataset2['col_0'] = dataset2['col_0'].astype('int32')

print(dataset2) 
print(dataset2.dtypes)
#  dataset2.apply(np.sum, axis=6)
dataset2.iloc[7]
dataset2.iloc[7][6]





