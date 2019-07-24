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

shou = [ ]
highs = []
lows = []
DIFS=[]
DEAS=[]
MACDS=[]
INCREASES = []
shou.reverse()


def getDetail_Data():
    Stock_Year_Detail_Url = d.Great_Detail.day_data('6038671')
    mm = d.Http_Request()
    request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
    while True:
        try:
            html = urllib.request.urlopen(request)
            data = re.search(r'(\()+([\d\D]*)',html.read().decode('utf-8')).group()[1:-1]
            for s in json.loads(data)["data"]:
                shou.append(s.split(',')[2])
                highs.append(s.split(',')[3])
                lows.append(s.split(',')[4])
            break
        except:
            pass

class GET_DIFandDEAandMACD():
    def getDIF(X, N):  # 通过12日EMA和26日EMA差值计算DIF
        if X == 0:
            return float(shou[X])
        return 2 / (N + 1) * float(shou[X]) + (1 - (2 / (N + 1))) * GET_DIFandDEAandMACD.getDIF(X - 1, N)
    def getDEA(X,N):
        if X==0:
            return 0.0
        return float(DIFS[X])*(2/(N+1))+(1-(2/(N+1)))*GET_DIFandDEAandMACD.getDEA(X-1,N)

    def getMACD(dif,dea):
        return (dif-dea)*2

    def GET_ALL(data):
        DIFS.clear()
        DEAS.clear()
        MACDS.clear()
        for s in range(len(data)):
            DIF = numpy.round(GET_DIFandDEAandMACD.getDIF(s, 12) - GET_DIFandDEAandMACD.getDIF(s, 26), decimals=3)
            DIFS.append(DIF)
            DEA = numpy.round(GET_DIFandDEAandMACD.getDEA(s, 9), decimals=3)
            DEAS.append(DEA)
            MACDS.append(numpy.round(GET_DIFandDEAandMACD.getMACD(DIF, DEA), decimals=3))
        print(DIFS)
        print(DEAS)
        print(MACDS)

class GET_RSI():
    def counter_diff(data,X):
        INCREASES.clear()
        data.reverse()
        print(shou)
        for s in range(len(data)):  # 计算差价
            if s == len(shou) - 1:
                increase = 0
            else:
                increase = float(data[s]) - float(data[s + 1])
                # increase = float(((float(shou[s])-float(shou[s+1]))/float(shou[s+1])))*100 #计算涨幅
            INCREASES.append(increase)
        INCREASES.reverse()
        GET_RSI.counter_RSI(X)

    def URS(N, X):
        if N == 0:
            return 0.0
        if (INCREASES[N] > 0):
            return GET_RSI.URS(N - 1, X) * (X - 1) / X + float(INCREASES[N]) / X
        else:
            return GET_RSI.URS(N - 1, X) * (X - 1) / X

    def DRS(N, X):
        if N == 0:
            return 0.0
        if (INCREASES[N] < 0):
            return GET_RSI.DRS(N - 1, X) * (X - 1) / X + abs(float(INCREASES[N])) / X
        else:
            return GET_RSI.DRS(N - 1, X) * (X - 1) / X

    def counter_RSI(X):
        for s in range(len(INCREASES)):
            urs = GET_RSI.URS(s, X)
            drs = GET_RSI.DRS(s, X)
            try:
                RS = urs / drs
                RSI = (RS / (1 + RS)) * 100
            except ZeroDivisionError:
                RSI = 100
            print(numpy.round(RSI, decimals=2))


def getK(num,total):
    #东方财富没有默认k值为50
    if(num!=-1):
        start = total-num
        nine_max = float(max(highs[start:start+9]))
        nine_min = float(min(lows[start:start+9]))
        shou_price = float(shou[num])
        try:
            RSV = (shou_price-nine_min)*100/(nine_max-nine_min)
        except ZeroDivisionError:
            RSV = 0.0
        if RSV==100 and num==0:
            return 100
        #print(str(RSV)+"||"+str(nine_max)+"||"+str(nine_min)+"||"+str(shou_price))
        elif num==0 and RSV!=0.0 and RSV!=100:
            return 1/3*RSV+50
        K = 2/3*getK(num-1,total) + 1/3*RSV
        if K>100:
            return 100
        return numpy.round(K, decimals=2)
    return 0

start= datetime.datetime.now()
getDetail_Data()
#GET_RSI.counter_diff(shou,6)
#GET_DIFandDEAandMACD.GET_ALL(shou)

highs.reverse()
lows.reverse()
for s in range(len(shou)):
    print(getK(s, len(shou) - 1))
end=datetime.datetime.now()
print('--运行时间: %s秒--'%(end-start))
#array = np.array(data)



