from urllib import request
import ssl
import json
import urllib
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.parse
import data_config

#东方财富股票的get请求,network抓包
detail_url = "http://64.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124001651461580406255_1561992580766&pn=1&pz=3754&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f2,f12,f14,f13&_=1561992580767"
# 爬虫抓取网页函数
def getHtml(url):
    mm=data_config.Http_Request()
    request = urllib.request.Request(url, headers=mm.get_header())
    html = urllib.request.urlopen(request).read().decode('utf-8')
    pos_start = html.find("[")#截取以'['开头的
    pos_end = html.find("]")
    data = html[pos_start:pos_end+1]#将内容以所示条件剪切
    return data

stocks,temp = [],{}
code =json.loads(getHtml(detail_url))
for name in code:
    if(name["f2"]!="-" and name["f2"]<200):#所有未退市的低于140元的股票
        temp["stock_code"]=name["f12"]#写入字典
        temp["stock_name"]=name["f14"]#写入字典
        temp["secid"]=name["f13"]#写入字典
        if(str(name["f12"])[:3]=="300" or str(name["f12"])[:3]=="002" or str(name["f12"])[:3]=="000"):
            temp["mk"]=2  #看个股月线时有用：2代表深圳，1代表上海
        else:
            temp["mk"]=1
        stocks.append(temp.copy())#将字典存入列表以组成json，必须用copy()
        temp.clear()#再清空，因为一次存一个
#存入json文件
with open("stocks.json",'w') as f:
    json.dump(stocks, f, ensure_ascii=False, indent=4)#第二个参数是防止中文乱码，第三个参数是排列

#读取股票数
with open('project_file/stocks.json') as j:
    count = json.load(j)
print(len(count))
#fhandle = open("./baidu.html", "wb") 创建新的文件
