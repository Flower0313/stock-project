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
RSIS = []
MACDS=[]
INCREASES = []
KS = []
DS = []
JS = []
BIAS = []
WRS =[]
MA=[]
VOL = []
OBV=[]
CCI=[]
ROC=[]
MAROC=[]  #6天一周期
PDI=[]
MDI=[]
ADX=[]

shou.reverse()


def getDetail_Data(code,methods):
    shou.clear()
    highs.clear()
    lows.clear()
    Stock_Year_Detail_Url = d.Great_Detail.day_data(code)
    mm = d.Http_Request()
    request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
    while True:
        try:
            html = urllib.request.urlopen(request)
            data = re.search(r'(\()+([\d\D]*)',html.read().decode('utf-8')).group()[1:-1]
            for s in json.loads(data)["data"]:
                temps = s.split(',')
                shou.append(temps[2])
                highs.append(temps[3])
                lows.append(temps[4])
                VOL.append(temps[5])
            if(methods=="MACD"):
                GET_DIFandDEAandMACD.GET_ALL(shou)
            elif(methods[:3]=="RSI"):
                GET_RSI.counter_diff(shou,int(methods[3:]))
            elif(methods=="KDJ"):
                GET_KDJ.Begin_KD(shou)
            elif(methods[:4]=="BIAS"):
                GET_BIAS.Begin_bias(shou,int(methods[4:]))
            elif(methods[:2]=="WR"):
                GET_WR.Begin_WR(shou,int(methods[2:]))
            elif(methods[:2]=="MA"):
                GET_MA.Begin_MA(shou,int(methods[2:]))
            elif(methods=="OBV"):
                GET_OBV.Begin_OBV(shou)
            elif(methods=="CCI"):
                GET_CCI.Begin_CCI(shou)
            elif(methods=="ROC"):
                GET_ROC.Begin_ROC(shou)
            elif(methods=="DMI"):
                GET_DMI.Begin_DMI(shou,highs,lows)
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
        #print(shou)
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
            RSIS.append(numpy.round(RSI, decimals=2))
        print(RSIS)

class GET_KDJ():
    def getKD(num,total):
        #东方财富没有默认k值为50
        if(num!=-1):
            start = total-num
            nine_max = float(max(highs[start:start+9]))
            nine_min = float(min(lows[start:start+9]))
            shou_price = float(shou[num])
            try:
                RSV = (shou_price-nine_min)*100/(nine_max-nine_min)
            except ZeroDivisionError:
                DS.append(0.0)
                RSV = 0.0
            if RSV==100 and num==0:
                DS.append(100.0)
                return 100.0
            elif num==0 and RSV!=0.0 and RSV!=100:
                K_temp = 1/3*RSV+50
                DS.append(K_temp)
                return K_temp
            K = 2/3*GET_KDJ.getKD(num-1,total) + 1/3*RSV
            D = numpy.round(1/3*K+2/3*DS[num-1],decimals=2)
            if K>100:
                DS.append(100)
                return 100
            elif len(DS)<=num:
                DS.append(D)
            return numpy.round(K, decimals=2)
        return 0

    def Count_J(KS,DS):
        for S in range(len(KS)):
            JS.append(numpy.round(3*KS[S] - 2*DS[S],decimals=3))


    def Begin_KD(data):
        KS.clear()
        DS.clear()
        JS.clear()
        highs.reverse()
        lows.reverse()
        for s in range(len(data)):
            KS.append(GET_KDJ.getKD(s, len(data) - 1))
            if (s != len(data) - 1):
                DS.clear()
        GET_KDJ.Count_J(KS,DS)
        print(KS)
        print(DS)
        print(JS)


def getDIF(X, N):  # 通过12日EMA和26日EMA差值计算DIF
    if X == 0:
        return float(shou[X])
    return 2 / (N + 1) * float(shou[X]) + (1 - (2 / (N + 1))) * GET_DIFandDEAandMACD.getDIF(X - 1, N)
def getDEA(X,N):
    if X==0:
        return 0.0
    return float(DIFS[X])*(2/(N+1))+(1-(2/(N+1)))*GET_DIFandDEAandMACD.getDEA(X-1,N)

class GET_BIAS():
    def get_bias(data,N,C):
        if(N>=(C-1)):
            num = 0
            for s in range(C):
                num+=float(data[N-s])
            bias = (float(data[N])-(num/C))/(num/C)*100
            return numpy.round(bias,decimals=3)
        else:
            return 0

    def Begin_bias(data,C):
        BIAS.clear()
        for s in range(len(data)):
            BIAS.append(GET_BIAS.get_bias(data, s, C))
        print(BIAS)

class GET_WR():
    def get_WR(N,X):
        shou_price=shou[N]
        if N<X:
            ring = 0
            N-1
        else:
            ring = N-X+1

        max_price = float(max(highs[ring:N+1]))
        min_price = float(min(lows[ring:N+1]))
        try:
            WR = (float(shou_price)-max_price)*100/(max_price-min_price)
        except ZeroDivisionError:
            WR = 0.0
        return numpy.round(WR,decimals=3)

    def Begin_WR(data,C):
        WRS.clear()
        for s in range(len(data)):
            WRS.append(GET_WR.get_WR(s, C))
        print(WRS)

class GET_MA():
    def get_MA(data,N,C):
        if (N >= (C - 1)):
            num = 0
            for s in range(C):
                num += float(data[N - s])
            ma =num/C
            return numpy.round(ma, decimals=2)
        else:
            return 0

    def Begin_MA(data,C):
        MA.clear()
        for s in range(len(data)):
            MA.append(GET_MA.get_MA(shou, s, C))
        print(MA)


class GET_OBV():
    def get_OBV(shou,vol,N):
        if(N!=0):
            if shou[N]>shou[N-1]:
                return GET_OBV.get_OBV(shou,vol,N-1)+float(VOL[N])
            elif shou[N]<shou[N-1]:
                return GET_OBV.get_OBV(shou,vol,N-1)-float(VOL[N])
            else:
                return GET_OBV.get_OBV(shou,vol,N-1)
        return 0.0

    def Begin_OBV(data):
        OBV.clear()
        for s in range(len(data)):
            OBV.append(GET_OBV.get_OBV(data, VOL, s))
        print(OBV)

class GET_CCI():
    def get_cci(shou,N):
        if(N>=14):
            num = 0
            typs=[]
            md=0
            for s in range(14):
                typ = (float(highs[N-1-s])+float(shou[N-1-s])+float(lows[N-1-s]))/3
                typs.append(typ)
                num+=typ
            num=num/14
            for s in range(14):
                md+=abs(num-typs[s])
            md=md/14
            return numpy.round((float(typs[0])-num)/(md*0.015),decimals=2)
        return 0.0

    def Begin_CCI(data):
        CCI.clear()
        for s in range(len(data)):
            CCI.append(GET_CCI.get_cci(shou, s))
        print(CCI)

class GET_ROC():
    def get_ROCandMAROC(data,N):
        if N!=0:
            if N<=11:
                pre_day = float(data[0])
            else:
                pre_day = float(data[N-11])
            now_day =float(data[N])
            roc = numpy.round((now_day-pre_day)*100/pre_day,decimals=3)
            ROC.append(roc)
            if N>=5:
                six_num = 0
                for s in range(6):
                    six_num+=ROC[N-s]
                MAROC.append(numpy.round(six_num/6,decimals=2))
            else:
                MAROC.append(0.0)
            return
        ROC.append(0.0)

    def Begin_ROC(data):
        ROC.clear()
        MAROC.clear()
        for s in range(len(data)):
            GET_ROC.get_ROCandMAROC(data, s)
        print(ROC)
        print(MAROC)

class GET_DMI():
    def get_DMI(data,highs,lows,N):
        if N<=13:
            MDI.append(0.0)
            PDI.append(0.0)
            ADX.append(0.0)
            return
        PDI_num = 0
        MDI_num =0
        tr_num = 0
        dx_num = 0

        for s in range(14):
            if s==13 and N==14:
                hd = 0
                ld=0
            else:
                hd =float(highs[(N-1)-s])-float(highs[(N-1)-(s+1)])
                ld = float(lows[(N-1)-s])-float(lows[(N-1)-(s+1)])
            if hd>0 :
                PDI_num+=hd
            elif ld<0:
                MDI_num+=abs(ld)

        for s in range(14):
            A = float(highs[(N-1)-s])-float(lows[(N-1)-s])
            if s==13 and N==14:
                B=0
                C=0
            else:
                B = abs(float(highs[(N-1)-s])-float(data[(N-1)-(s+1)]))
                C = abs(float(lows[(N-1)-s])-float(data[(N-1)-(s+1)]))
            if A > B:
                if A>C:
                    tr = A
                else:
                    tr = C
            else:
                if B>C:
                    tr =B
                else:
                    tr = C
            tr_num+=tr
        PDI.append(numpy.round(((PDI_num))*100/(tr_num),decimals=2))
        MDI.append(numpy.round(((MDI_num))*100/(tr_num),decimals=2))
        if N<=18:
            ADX.append(0.0)
        else:
            for s in range(6):
                try:
                    dx_num += (abs(float(PDI[N-1-s]) - float(MDI[N-1-s]))) * 100 / (float(PDI[N-1-s]) + float(MDI[N-1-s]))
                except:
                    dx_num+=0
            ADX.append(dx_num/6)

    def Begin_DMI(data,highs,lows):
        MDI.clear()
        PDI.clear()
        ADX.clear()
        for s in range(len(shou)):
            GET_DMI.get_DMI(data, highs, lows, s + 1)
        print(PDI)
        print(MDI)
        print(ADX)
start= datetime.datetime.now()

getDetail_Data('6038631',"DMI")


# get_DMI(shou,highs,lows,14)

# getDetail_Data('6038631',"KDJ")
#getDetail_Data('6038671',"BIAS12")




end=datetime.datetime.now()
print('--运行时间: %s秒--'%(end-start))
#array = np.array(data)



