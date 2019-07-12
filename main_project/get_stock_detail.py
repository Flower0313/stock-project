import json
from urllib import request
import ssl
import urllib
import urllib.parse
import project_files.data_config as d
import re
import datetime
import threading
import time
import urllib.error
from queue import Queue

ssl._create_default_https_context = ssl._create_unverified_context

def get_detail(secid,code_number,qq):
    #fltt是控制小数点的，secid是控制股票代号
    url = d.Get_Detail_Info_Url+'secid='+str(secid)+'.'+str(code_number)
    code =json.loads(getHtml(url))
    qq.put(d.Choose_detail.judge_one(code))
    #print(code['f58'])

def getHtml(url):#获取个股详细字典
    global res
    mm=d.Http_Request()
    request = urllib.request.Request(url, headers=mm.get_header())
    try:
        html = urllib.request.urlopen(request,timeout=10)
        res = re.search(r"(:{1})+(\{.+\})", html.read().decode('utf-8')).group()[1:-1]
    except:
        exPool = True
        while exPool:
            try:
                time.sleep(3)
                # print("----------------------------------------")
                html = urllib.request.urlopen(request,timeout=10)
                res = re.search(r"(:{1})+(\{.+\})", html.read().decode('utf-8')).group()[1:-1]
                exPool = False
            except:
                pass
    return res

#筛选算法---核心---
def stock_filter(data):
        if(data["涨幅"]>3):
            print("%s:%s%%" % (data["股票"], data["涨幅"]))

start= datetime.datetime.now()#开始时间
num=0
with open('stocks.json') as j:
    q=Queue()#只能用queue来取出thread中的值
    threads=[]
    for sc in json.load(j):
        num=num+1;
        t1 = threading.Thread(target=get_detail, args=(sc['secid'],sc['stock_code'],q))
        t1.start()
        threads.append(t1)
    results=[]
    for s in range(num):
        print(q.get()["股票"]+str(s))
    print("--------总计算量:%d--------" % num)
end=datetime.datetime.now()#结束时间
print('--运行时间: %s秒--'%(end-start))
