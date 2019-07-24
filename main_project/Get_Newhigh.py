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

ssl._create_default_https_context = ssl._create_unverified_context
lock=threading.Lock()
def getHtml(name,code,mk,qq):#获取每个股票的月线详情
    Stock_Year_Detail_Url = "http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&" \
                            "cb=jQuery18306381636561594661_1562731154930&id=" + code + mk + "&type=mk&authorityType=&_=1562731160889"

    mm = d.Http_Request()
    request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
    while True:
        try:
            html = urllib.request.urlopen(request, timeout=None)
            data = re.search(r"(\[.+\])", html.read().decode('utf-8')).group()
            break
        except Exception as e:
            time.sleep(3)
            # if(str(e)=="'NoneType' object has no attribute 'group'"):
            #     break
            #print("-----------------1"+name+"1------------------")
            pass
    #print(name+code+"\\"+str(data))
    qq.put(name+code+Compare_stock(data))
    #urllib.error.URLError
    #socket.timeout: timed out
    #AttributeError

#开始函数
def List_Stocks():#先条用getHtml()再条用Compare_stock()
    num = 0
    results = []
    with open("stocks.json","r") as j:
        q = Queue()
        threads = []
        for sc in json.load(j):
            num=num+1
            t1=threading.Thread(target=getHtml,args=(sc["stock_name"],sc["stock_code"],str(sc["mk"]),q),)
            t1.start()
            threads.append(t1)
        # for _ in threads:
        #     t1.join()
        print("------以下为创历史新高的股票------")
        for _ in threads:
            temp = q.get(block=True,timeout=None)
            if(temp[-1]=="1"):
                print(temp[:-1])
            #results.append(q.get(block=True,timeout=None))
    #for s in results:
         # if(str(s)[-1]=="1"):
         #     print(str(s)[:-1])
    print("--------总计算量：%d--------"%num)

def Compare_stock(data):#比较股票是否创新高
    #创历史新高返回1，没有则返回0
    Now_data=json.loads(data)
    now_price = Now_data[-1].split(',')[2]
    for line in Now_data:
        #print(line.split(',')[2])
        if(float(line.split(',')[2])>float(now_price)):
            return "0"
        else:
            continue
    return "1"

start= datetime.datetime.now()#开始时间
List_Stocks()
end=datetime.datetime.now()#结束时间
print('--运行时间: %s秒--'%(end-start))


