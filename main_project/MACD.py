# coding=gbk
import threading
import time
from queue import Queue
from urllib import request
import ssl
import json
import urllib.parse
import project_files.data_config as d
import datetime
import re
import urllib
import sys
import numpy
sys.setrecursionlimit(1000000)

ssl._create_default_https_context = ssl._create_unverified_context

shou = []
DIFS=[]
DEAS=[]
MACDS=[]

def getDetail_Data():

    Stock_Year_Detail_Url = "http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?token=4f1862fc3b5e77c150a2b985b12db0fd&rtntype=6&id=0001002&type=k&authorityType=fa&cb=jsonp1563531034531"
    mm = d.Http_Request()
    request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
    html = urllib.request.urlopen(request)
    data = re.search(r'(\()+([\d\D]*)',html.read().decode('utf-8')).group()[1:-1]
    for s in json.loads(data)["data"]:
        shou.append(s.split(',')[2])

def getDIF(X,N):#通过12日EMA和26日EMA差值计算DIF
    if X==0:
        return float(shou[X])
    return 2/(N+1)*float(shou[X]) + (1-(2/(N+1)))*getDIF(X-1,N)


def getDEA(X,N):
    if X==0:
        return 0.0
    return float(DIFS[X])*(2/(N+1))+(1-(2/(N+1)))*getDEA(X-1,N)

def getMACD(dif,dea):
    return (dif-dea)*2

start= datetime.datetime.now()
getDetail_Data()
count = len(shou)
for s in range(count):
    DIF =numpy.round(getDIF(s,12)-getDIF(s,26),decimals=3)
    DIFS.append(DIF)
    DEA = numpy.round(getDEA(s,9),decimals=3)
    DEAS.append(DEA)
    MACDS.append(numpy.round(getMACD(DIF,DEA),decimals=3))
print(DIFS)
print(DEAS)
print(MACDS)
end=datetime.datetime.now()
print('--运行时间: %s秒--'%(end-start))



