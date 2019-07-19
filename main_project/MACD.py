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
import demjson
import sys
sys.setrecursionlimit(1000000)

ssl._create_default_https_context = ssl._create_unverified_context

Stock_Year_Detail_Url = "http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?token=4f1862fc3b5e77c150a2b985b12db0fd&rtntype=6&id=0001002&type=k&authorityType=fa&cb=jsonp1563531034531"
mm = d.Http_Request()
request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
html = urllib.request.urlopen(request)
data = re.search(r'(\()+([\d\D]*)',html.read().decode('utf-8')).group()[1:-1]
shou = []
for s in json.loads(data)["data"]:
    shou.append(s.split(',')[2])
count = len(shou)


def counterEMA(X,N):
    if X==0:
        return float(shou[X])
    else:
        return 2/(N+1)*float(shou[X]) + (1-(2/(N+1)))* counterEMA(X-1,N)


print("DIF:"+str(round(counterEMA(count-1,12)-counterEMA(count-1,26),3)))

