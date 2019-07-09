import threading
import time
import threading
import time
from queue import Queue
import random
import urllib
from urllib import request


for i in range(0,10):
    try:
        data = urllib.request.urlopen("http://www.baidu.com",timeout=0.01).read()
        print(len(data))
    except Exception as e:
        print("出现异常:"+str(e))
