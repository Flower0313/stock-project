import json
from urllib import request
import ssl
import urllib
import urllib.parse
import data_config
import re
import unittest
import datetime
import threading
import socket
import time
import urllib.error
import random
import os
from queue import Queue
ssl._create_default_https_context = ssl._create_unverified_context

def get_detail(secid,code_number,qq):
    #fltt是控制小数点的，secid是控制股票代号
    url ='http://push2.eastmoney.com/api/qt/stock/get?&fltt=2&fields=f43,f57,f58,f169,f46,f44,f51,f168,f47,f60,f45,f116,f117,f52,f50,f48,f167,f71,f49,f60,f137,f188,f105,f173,f186,f195,f196,f43,f197&' \
         'secid='+str(secid)+'.'+str(code_number)
    code =json.loads(getHtml(url))
    #return data_config.Choose_detail.judge_one(code)
    qq.put(code['f58'])
    #return(code['f58'])

def getHtml(url):#获取个股详细字典
    global res
    Pool = False
    time.sleep(0.1)
    mm=data_config.Http_Request()
    request = urllib.request.Request(url, headers=mm.get_header())
    try:
        html = urllib.request.urlopen(request)
        res = re.search(r"(:{1})+(\{.+\})", html.read().decode('utf-8')).group()[1:-1]
    except urllib.error.URLError:
        Pool = True
        while Pool:
            try:
                time.sleep(3)
                #print("----------------------------------------")
                html = urllib.request.urlopen(request)
                res = re.search(r"(:{1})+(\{.+\})", html.read().decode('utf-8')).group()[1:-1]
                Pool=False
            except:
                Pool=True
    return res
# for k,v in data_config.Choose_detail.judge_one(code).items():
#     print(k+"："+str(v))


#输出所有股票代码
# with open('stocks.json') as j:
#     for sc in json.load(j):
#         print(get_detail(sc['secid'],sc['stock_code']))

start= datetime.datetime.now()#开始时间
num=0
with open('stocks.json') as j:
    q=Queue()#只能用queue来取出thread中的值
    threads=[]
    for sc in json.load(j):
        num=num+1;
        t1 = threading.Thread(target=get_detail, args=(sc['secid'],sc['stock_code'],q), name="T1")
        t1.start()
        threads.append(t1)
    results=[]
    for s in range(num):
        print(q.get()+str(s))
    print(num)
end=datetime.datetime.now()#结束时间
print('运行时间: %s 秒'%(end-start))
