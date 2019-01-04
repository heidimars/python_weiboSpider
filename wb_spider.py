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
for user_id in list1[0:len(list1)]:
    #cookie需替换成本人的！
    cookie = {"Cookie": "_T_WM=044464d9eabaf0af138f4f2ad6535bc7; SCF=ApXgMGDQIU-m06wgW9qlwwehnKfSGXvLguigDfsI39zH0Oms21cdeVv8ZnYA0l6r-G53lOPSXTqGWjnNfhHC1G4.; SUB=_2A25xDwv7DeRhGeVP7lAY8y3EzTyIHXVS85WzrDV6PUJbkdAKLWbikW1NTOasS0BksgTX68JisJJRy-KbYFjxCPFh; SUHB=0YhRlN-ngr2_3e; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D20000174"}
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
    file_dir = os.path.split(os.path.realpath(__file__))[0] + os.sep + "weibo_jy"
    if not os.path.isdir(file_dir):
        os.mkdir(file_dir)
    file_path = file_dir + os.sep + "%d" % int(user_id) + ".txt"
    fo = open(file_path, "wb")
    fo.write(result.encode(sys.stdout.encoding))
    word_path=os.getcwd()+'/%d'%int(user_id)
    fo.close()
print ('文字微博爬取完毕') 
