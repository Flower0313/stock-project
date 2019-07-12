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
import aiohttp
import asyncio

async def get_stock(code):
    url = 'http://hq.sinajs.cn/list=' + code
    resp = await aiohttp.request('GET', url) # yield
    body = await resp.read()
    text = body.decode('gb2312')
    print(text)
    resp.close()

codes = ['sz000878', 'sh600993', 'sz000002', 'sz002230']
tasks = [get_stock(code) for code in codes]
print(tasks)


