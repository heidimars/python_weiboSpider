# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:42:42 2018

@author: Administrator
"""
import sys
import requests
import json
import time
import random
import codecs
import importlib
import traceback

importlib.reload(sys)
infofile = codecs.open("Weibo_List_p.txt", 'a', 'utf-8')

def crawlDetailPage(url,page):
    global ID_get
    #global num
    global infofile
    #读取微博网页的JSON信息
    req = requests.get(url)
    jsondata = req.text
    data = json.loads(jsondata)
    #获取每一条页的数据
    content = data['data'].get('cards')
    
    #print(content)
    #循环输出每一页的关注者各项信息
    try:
        for i in content:
            followingId = i['user']['id']
            #print(followingId)
            ID_get.append(followingId)
            #num=num+1
            infofile.write(str(followingId)+ '\r\n')
    except Exception as e:
            print ("Error: ",e)
            traceback.print_exc()


user_oid=1005052766134004   #另一个的是： 1005055984336074

ID_get = [];
for i in range(1, 501):
    print("正在获取第{}页的粉丝列表:".format(i))
    # 微博用户关注列表JSON链接
    url = "https://m.weibo.cn/api/container/getSecond?containerid={user_oid}_-_FANS&page={page}".format(user_oid=user_oid, page=i)  # page=" +   #FOLOWERS关注，FANS粉丝
    crawlDetailPage(url, i)
        # 设置休眠时间
    t = random.randint(2, 5)
    print("休眠时间为:{}s".format(t))
    time.sleep(t)


