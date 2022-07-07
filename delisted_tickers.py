#  import libs 
from cgitb import text
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


# having API, get API (json form)
# 1 - delisted tickers
# x = 2018-2022

# years = ('2018','2019','2020','2021')
# for year in years:
delisted_url = ("https://www.hsx.vn/Modules/Listed/Web/CancelledStockList"
           "?y=" + "2019" + "&_search=false&nd=1655972641925&rows=30&page=1&sidx=id&sord=desc")

resp = requests.get(delisted_url)
resul = resp.json()
print(resp) #check api status 200 is OK
print(resul)

resul.keys() #check params key in json

data = resul['rows']
print(data)

print(resul['total'])
print(len(data))

#turn json to dataset 
DATASET = []
for i in range(int(resul['total'])) :
    dataset = []
    for a in range(len(data)):
        record = data[a]
        record_cell = record['cell']
        dataset.append(record_cell)
*DATASET, =dataset #using packing value whit operator '*'
    # DATASET.append(dataset) #2 rows (loop 2 total) and 30 columns bcs using append
nice = pd.DataFrame(dataset)
print(nice)
print('-------------------')
dataset2 = pd.DataFrame(DATASET, columns=['stt','tickers_href','isin','figi','company_name','delist_date','volume'])
# change datatype from object to fit in columns
    # dataset2.astype({0:'int32'}).dtypes
dataset2.info()
# dataset2['col_0'] = dataset2['col_0'].astype('int32')

print(dataset2) 
print(dataset2.dtypes)
#  dataset2.apply(np.sum, axis=6)
dataset2.iloc[29]
dataset2.iloc[29][2]

href = dataset2.iloc[:,1]  # select column containing href attribute
dataset2.iloc[:,1][3]

# html -> attribute href => lay id


# use beautifulsoup to get id from href attribute
# soup.find_all('a')


# Element-Wise -> Ap dung cho tung phan du lieu tren 1 record


def extract_link(link_href):
    
    soup = BeautifulSoup(link_href)

    soup.prettify()

    output = soup.find_all('a')[0].get('href')

    tickers = re.search('\d+$', output).group()
    return tickers

# extract_link("<a href='/Modules/Listed/Web/SymbolView?id=799'>CFPT1903            </a>")
# link_test = "<a href='/Modules/Listed/Web/SymbolView?id=799'>CFPT1903            </a>"
# soup = BeautifulSoup(link_test)
# soup.prettify()
# output = soup.find_all('a')[0]
# output_1 = str(output).split(">")
# print(output_1)

tickers = pd.DataFrame(DATASET).iloc[:, 1].apply(
        func=extract_link)
print(tickers)
dataset2['ticker_id'] = tickers
print(dataset2)
dataset2.info()


