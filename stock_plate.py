import json
from urllib import request
import ssl
import urllib
import urllib.parse
import data_config
import re
import datetime
import threading
import time
import urllib.error
from queue import Queue

Plate_Url='http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124018031994186919387_1562640559933&pn=1&pz=20&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&' \
          'fs=m:90+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107,f104,f105,f140,' \
          'f141,f207,f222&_=1562640559934'


def get_plate(url):#获取个股详细字典
    global res
    exPool = True
    mm=data_config.Http_Request()
    request = urllib.request.Request(url, headers=mm.get_header())
    while exPool: #循环抓取直到没异常发生
        try:
            html = urllib.request.urlopen(request,timeout=5)
            res = re.search(r"\{+(\"{1})+\d+(\"{1})+(:{1})+(\{.+\})", html.read().decode('utf-8')).group()[:-2]
            exPool = False
        except:
            time.sleep(3)
            continue
    return res

print(get_plate(Plate_Url))