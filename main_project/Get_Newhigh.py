import threading
import time
import threading
import time
from queue import Queue
from urllib import request
import ssl
import json
import urllib.parse
import project_file.data_config
import datetime
import re
import urllib


ssl._create_default_https_context = ssl._create_unverified_context

def getHtml(code,secid,qq):#获取每个股票的月线详情
    Stock_Year_Detail_Url = "http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&" \
                            "cb=jQuery18306381636561594661_1562731154930&id="+code+secid+"&type=mk&authorityType=&_=1562731160889"
    mm=data_config.Http_Request()
    request = urllib.request.Request(Stock_Year_Detail_Url, headers=mm.get_header())
    try:
        html = urllib.request.urlopen(request, timeout=10)
        data = re.search(r"(\[.+\])", html.read().decode('utf-8')).group()
    except:
        exPool = True
        while exPool:
            try:
                time.sleep(3)
                # print("----------------------------------------")
                html = urllib.request.urlopen(request, timeout=10)
                data = re.search(r"(\[.+\])", html.read().decode('utf-8')).group()
                exPool = False
            except:
                pass
    qq.put(Compare_stock(data))


def List_Stocks():#先条用getHtml()再条用Compare_stock()
    with open("..\stocks.json","r") as j:
        q = Queue()
        threads = []
        for sc in json.load(j)[:1]:
            t1=threading.Thread(target=getHtml,args=(sc["stock_code"],str(sc["mk"]),q),)
            t1.start()
            threads.append(t1)
            #Compare_stock(getHtml(sc["stock_code"],str(sc["mk"])))
        print(q.get())
def Compare_stock(data):#比较股票是否创新高
    Now_data=json.loads(data)
    now_price = Now_data[-1].split(',')[2]
    num = 0
    for line in Now_data:
        if(float(line.split(',')[2])>float(now_price)):
            return "不是历史最高"
            num=1
            break
        else:
            continue
    if(num==0):
        return "是历史最高"

start= datetime.datetime.now()#开始时间
#print(Compare_stock(getHtml("000100",'2')))
List_Stocks()
# with open('stocks.json') as j:
#     threads=[]
#    # for sc in json.load(j):
#
#     print("--------总计算量:%d--------" % num)
end=datetime.datetime.now()#结束时间
print('--运行时间: %s秒--'%(end-start))

# with open("project_file/New_high.json") as f:
#     #f.write(getHtml(Stock_Year_Detail_Url))#第二个参数是防止中文乱码，第三个参数是排列
#     ff=json.loads(f.read())


