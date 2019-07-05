import threading
import time
import threading
import time
from queue import Queue
import random


# def sayhi(num):  #定义每个线程要运行的函数
#     print('running on number'+str(num)+'\n')
#     time.sleep(3)
#
# t1 = threading.Thread(target=sayhi,args=(33,),name="t1") #生成一个线程实例
# t2 = threading.Thread(target=sayhi,args=(22,),name="t2") #生成另一个线程实例
#
# t1.start()  #启动线程
# t2.start()
# print("t1线程名："+t1.getName()) #获取线程名
# print("t2线程名："+t2.getName())
# t1.join()  #阻塞主线程，等待t1子线程执行完后再执行后面的代码
# t2.join()  #阻塞主线程，等待t2子线程执行完后再执行后面的代码
# print('-----end')

ip = ['121.31.159.197', '175.30.238.78', '124.202.247.110']
headerss = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'X-Forwarded-For': ip[random.randint(0, 2)]}
print(headerss)