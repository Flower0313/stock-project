from urllib import request
import ssl
import json
import urllib
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.parse

header = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Language":" zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "qgqp_b_id=55443a383a2142c4e4e466da95538cc7; st_si=90641855213591; st_asi=delete; st_pvi=42443299630348; st_sp=2019-07-01%2018%3A14%3A55; st_inirUrl=; st_sn=11; st_psi=20190701220622893-113200301321-8492325806; HAList=a-sz-300362-%u5929%u7FD4%u73AF%u5883; em_hq_fls=js",
"Host": "quote.eastmoney.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
#东方财富股票的get请求,network抓包
detail_url = "http://64.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124001651461580406255_1561992580766&pn=1&pz=3754&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2&fields=f12,f14&_=1561992580767"
# 爬虫抓取网页函数
def getHtml(url):
    request = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(request).read().decode('utf-8')
    pos_start = html.find("[")#截取以'['开头的
    pos_end = html.find("]")
    data = html[pos_start:pos_end+1]#将内容以所示条件剪切
    return data

stocks,temp = [],{}
code =json.loads(getHtml(detail_url))
for name in code:
    temp["stock_code"]=name["f12"]#写入字典
    temp["stock_name"]=name["f14"]#写入字典
    stocks.append(temp.copy())#将字典存入列表以组成json，必须用copy()
    temp.clear()#再清空，因为一次存一个
#存入json文件
with open("stocks.json",'w') as f:
    json.dump(stocks, f, ensure_ascii=False, indent=4)#第二个参数是防止中文乱码，第三个参数是排列

#fhandle = open("./baidu.html", "wb") 创建新的文件

$ 