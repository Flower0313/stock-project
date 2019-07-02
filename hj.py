#######################################
#时间：2019-6-23
#项目：不能当韭菜
#开发者：肖华
#######################################
from collections import OrderedDict
import json
import matplotlib.pyplot as plt
from random import randint
from die import Die
import pygal
import csv
import time
import pandas
from datetime import datetime
from pygal_maps_world.maps import COUNTRIES
from operator import itemgetter
import requests
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
# names = ['xiao','flower','xixi']
# names.insert(1,'hua') #指定位置插入元素
# names.append('haha') #在尾部插入元素
# print(names)
# del names[-1] #删除语句
# print(names)
# namesz = names.pop(1) #删除指定元素并赋值
# print(namesz)
# names.remove('xiao') #根据元素名删除指定元素
# print(names)
# names.sort(reverse=0) #按照字母序列排序打印
# print(names)
# names.reverse() #反转打印
# len(names) #获得列表的长度
# for name in names:  #for循环，记得冒号和缩进
#     print("名字："+name)
# numbers = list(range(2,11,2)) #从2开始每个加2，直到>=11结束并转换为列表

# squares = [value**2 for value in range(1,11)]
# print(squares)
# print(squares[:])
# numbers = (200,5,11)
# print(numbers[0])
# if (4 not in squares):
#     print("Bingo!")
# else:
#     print("Bad")
#
# alien_0={'color':'red','point':5} #字典,相当于Json数据
# alien_0['x_position']=0
# alien_0['y_position']=25
# for k in alien_0:
#     print(str(k))


class Dog():
    def __init__(self,name,age):
        self.name2 = name
        self.age3 = age
    def sit(self,one):
        print(str(one))

favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
# def greet_user(num): #形参前面加一个*是空元组，**是一个空字典
#     if (num==1 or num==2):
#         return 1
#     else:
#         return greet_user(num-1)+greet_user(num-2)
# print(greet_user(6))

# test = OrderedDict() #调用别的类，类似于字典
# test['name'] = 'flower'
# test['age'] = 14
# for k,v in test.items():
#     print(k+'和'+str(v))
#
# x = randint(1,6)
class RnadomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_v=[0]
        self.y_v=[0]

    def fill_walk(self):
        while len(self.x_v)<self.num_points:
            x_dir = random.choice([1,-1])
            x_dis = random.choice([0,1,2,3,4])
            x_step = x_dis * x_dir

            y_dir = random.choice([1, -1])
            y_dis = random.choice([0, 1, 2, 3, 4])
            y_step = y_dis * y_dir

            if x_step==0 and y_step==0:continue

            next_x = self.x_v[-1]+x_step
            next_y = self.y_v[-1]+y_step

            self.x_v.append(next_x)
            self.y_v.append(next_y)

# rw = RnadomWalk(50000)
# rw.fill_walk()
# point_numbers = list(range(rw.num_points))
# plt.scatter(rw.x_v, rw.y_v,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
# plt.scatter(0,0,c='yellow',edgecolors='none',s=100) #起点
# plt.scatter(rw.x_v[-1],rw.y_v[-1],c='red',edgecolors='none',s=100) #终点
# plt.xticks([])
# plt.yticks([])
# plt.show()

# die=Die()
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# frequencies = []
# for value in range(1,die.num_sides+1):
#     frequency=results.count(value)
#     frequencies.append(frequency)
#
# hist= pygal.Bar()
# hist.x_labels = [x for x in range(1,7)]
# hist.add('D6',frequencies)
# hist.render_to_file('die_visual.svg')

# filename = 'sitka_weather_2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     highs,lows,dates=[],[],[]
#     for row in reader:
#         dates.append(datetime.strptime(row[0],"%Y/%m/%d"))
#         highs.append(int(row[1]))
#         lows.append(int(row[3]))
# fig = plt.figure(dpi=128,figsize=(10,6))
# plt.plot(dates,highs,c='red')
# plt.plot(dates,lows,c='blue')
# plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# fig.autofmt_xdate()
# plt.tick_params(axis='both',which='major',labelsize=16)
# plt.show()

#世界地图
# def grt_country_code(c_name):
#     for code,name in COUNTRIES.items():
#         if(c_name==name):
#             return code
#     return None
#
# cc_pop = {}
# filename='population_data.json'
# with open(filename) as f:
#     pop_data = json.load(f)
# for pp in pop_data:
#     if pp['Year'] =='2010':
#         c_name = pp['Country Name']
#         poplution = int(float(pp['Value']))
#         code = grt_country_code(c_name)
#         if code:
#             cc_pop[code]=poplution
# cc1,cc2,cc3={},{},{}
# for cc,pop in cc_pop.items():
#     if pop<10000000:
#         cc1[cc]=pop
#     elif pop<1000000000:
#         cc2[cc]=pop
#     else:
#         cc3[cc]=pop
# wm = pygal.maps.world.World()
# wm.add('one', cc1)
# wm.add('two', cc2)
# wm.add('three', cc3)
# wm.render_to_file('amer.svg')

#17章API
# url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
# r=requests.get(url)
# print("Staus code:",r.status_code)
# response_dict = r.json()
#
# repo_ds = response_dict['items']
# names,stars=[],[]
# for rep in repo_ds:
#     names.append(rep['name'])
#     plot_dict={
#         'value':rep['stargazers_count'],
#         'label':rep['description'],
#         'xlink':rep['html_url'],
#     }
#     stars.append(plot_dict)
#
# #可视化
# my_style = LS('#333366',base_style=LCS)
# chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
# chart.x_labels=names
# chart.add('',stars)
# chart.render_to_file('pppp.svg')

all_stock = "http://quote.eastmoney.com/stocklist.html"
