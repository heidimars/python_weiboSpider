# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 17:15:52 2018

@author: Administrator
"""
#import re
#import string
import sys
import os
#import urllib
#import urllib2
#from bs4 import BeautifulSoup
import requests
from lxml import etree
import importlib
from requests.packages.urllib3.exceptions import InsecureRequestWarning 

import certifi
import urllib3
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())

importlib.reload(sys) 

#读取准备好了的userid文件
with open('Weibo_List_jy.txt', 'r') as f1:
    list1 = f1.readlines()
for i in range(0, len(list1)):
    list1[i] = list1[i].rstrip('\n')
for user_id in list1[0:10]:
    #cookie需替换成本人的！
    cookie = {"Cookie": "_T_WM=895f154bb45c806a94eeaf7b018b4305; ALF=1548851546; SCF=Ag5kkvZQykmazulxfh5RQhCKT0OYudxQqfK_EMxj0krZcONynSlpX1Fc5U3pDir1haP5X2n-_yvBB1PkQVTz8Ns.; SUB=_2A25xLnwMDeRhGeVP7lAY8y3EzTyIHXVS0QRErDV6PUNbktAKLWjYkW1NTOasSwijAzTFFUA4X0Np_uCdLbS25H5X; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF3nTRVeAZF9Ln3yKMkVU1N5JpX5KMhUgL.FoepSKz4e0eRSo52dJLoIEXLxK-L12-L1-qLxK-LB-BL1K5LxKBLBonL12-LxKqL1KnL1-qLxKMLBoeLB.zt; SUHB=09P9CNvMah6QYo"}
    url = 'http://weibo.cn/u/%d?filter=1&page=1'% int(user_id)
 
    html = requests.get(url, cookies = cookie).content
    selector = etree.HTML(html)
    controls = selector.xpath('//input[@name="mp"]')
    if controls:
        pageNum = int(controls[0].attrib['value'])
    
    result = "" 
    urllist_set = set()
    word_count = 1
 
    print ('爬虫准备就绪...')
 
    for page in range(1,pageNum+1):
 
        #获取lxml页面
        url = 'http://weibo.cn/u/%d?filter=1&page=%d'% (int(user_id),page) 
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        lxml = requests.get(url, cookies = cookie,verify=False).content
 
        #文字爬取
        selector = etree.HTML(lxml)
        content = selector.xpath('//span[@class="ctt"]')
        for each in content:
            text = each.xpath('string(.)')
            if word_count>=4:
                text = "%d :"%(word_count-3) +text+"\n\n"
            else :
                text = text+"\n\n"
            result = result + text
            word_count += 1
    file_dir = os.path.split(os.path.realpath(__file__))[0] + os.sep + "weibo_test"
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
    file_path = file_dir + os.sep + "%d" % int(user_id) + ".txt"
    fo = open(file_path, "wb")
    fo.write(result.encode(sys.stdout.encoding))
    word_path=os.getcwd()+'/%d'%int(user_id)
    fo.close()
print ('文字微博爬取完毕') 
