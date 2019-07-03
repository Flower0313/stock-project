
class Http_Request():
    headers={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Accept-Language":" zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Cookie": "qgqp_b_id=55443a383a2142c4e4e466da95538cc7; st_si=90641855213591; st_asi=delete; st_pvi=42443299630348; st_sp=2019-07-01%2018%3A14%3A55; st_inirUrl=; st_sn=11; st_psi=20190701220622893-113200301321-8492325806; HAList=a-sz-300362-%u5929%u7FD4%u73AF%u5883; em_hq_fls=js",
"Host": "quote.eastmoney.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

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
