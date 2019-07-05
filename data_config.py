
import random
class Http_Request():
    def get_header(self):
        ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110','223.150.185.153']
        header= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
            'X-Forwarded-For': ip[random.randint(0, 3)]}
        return header








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
        return temp_dic
