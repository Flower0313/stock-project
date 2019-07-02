import json
from urllib import request
import ssl
import urllib
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.parse
import data_config
import re

#读取有多少个股票数
# with open('stocks.json') as j:
#     count = json.load(j)
# print("股票数："+len(count))

url = 'http://push2.eastmoney.com/api/qt/stock/get?ut=000100&invt=2&fltt=2&fields=f43,f57,f58,f169,f46,f44,f51,f168,f47,f60,f45,f116,f117,f52,f50,f48,f167,f71,f49,f60,f137,f188,f105,f173,f186,f195,f196,f197&secid=0.000100&cb=jQuery18304467440863261962_1562051616309&_=1562051616982'

stock_details,temp=[],{}
def getHtml(url):
    request = urllib.request.Request(url, headers=data_config.Http_Request.headers)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    res = re.search(r"(:{1})+(\{.+\})", html).group()[1:-1]
    return res

code =json.loads(getHtml(url))
for k,v in code.items():
    print(k+'和'+str(v))