
import random
class Http_Request():
    def get_header(self):
        ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110','223.150.185.153','36.157.124.115','36.157.124.116','223.151.89.130']
        header= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
            'X-Forwarded-For': ip[random.randint(0, 3)]}
        return header

Get_Detail_Info_Url="http://push2.eastmoney.com/api/qt/stock/get?&fltt=2&fields=f43,f170,f57,f58,f169,f46,f44,f51,f168,f47,f60,f45," \
                    "f116,f117,f52,f50,f48,f167,f71,f49,f60,f137,f188,f105,f173,f186,f195,f196,f43,f197&"

Industry_Segments_Url="http://60.push2.eastmoney.com/api/qt/clist/get?cb=jQuery1124018031994186919387_1562640559933&pn=1&pz=61&" \
                      "ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:90+t:2&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10," \
                      "f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f124,f107,f104,f105,f140," \
                      "f141,f207,f222&_=1562640559934"
class Choose_detail:
    def judge_one(data):
        temp_dic = {}
        for k,v in data.items():
            if (k == 'f43'):
                temp_dic['现价'] = v
            if(k=='f44'):
                temp_dic['今开']=v
            elif(k=='f46'):
                temp_dic['最高']=v
            elif(k=='f45'):
                temp_dic['最低']=v
            elif(k=='f51'):
                temp_dic['涨停']=v
            elif(k=='f168'):
                temp_dic['换手']=v
            elif(k=='f47'):
                temp_dic['成交量']=v
            elif(k=='f52'):
                temp_dic['跌停']=v
            elif(k=='f50'):
                temp_dic['量比']=v
            elif(k=='f48'):
                temp_dic['成交额']=v
            elif(k=='f167'):
                temp_dic['市净']=v
            elif(k=='f117'):
                temp_dic['流通市值']=v
            elif(k=='f60'):
                temp_dic['昨收']=v
            elif(k=='f173'):
                temp_dic['ROE']=v
            elif(k=='f186'):
                temp_dic['毛利率']=v
            elif(k=='f105'):
                temp_dic['净利润']=v
            elif(k=='f188'):
                temp_dic['负债率']=v
            elif(k=='f58'):
                temp_dic['股票']=v
            elif (k == 'f170'):
                temp_dic['涨幅'] = v
            elif (k == 'f169'):
                temp_dic['涨跌价'] = v
        return temp_dic
