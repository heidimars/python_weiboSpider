# -*- coding: utf-8 -*-
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from wordcloud import WordCloud, ImageColorGenerator

# 获取当前文件路径
# __file__ 为当前文件
d = path.dirname(__file__)
# 读取文本 
#text = open('top_words.txt','r',encoding="gb2312").readlines()
fp=pd.read_csv('top_words.txt',encoding="gb2312",names=['name','val'])
name = list(fp.name)#词
value = fp.val#词的频率
for i in range(len(name)):
    name[i] = str(name[i])
      #因为要显示中文，所以需要转码
    name[i] = name[i]
dic = dict(zip(name, value))#词频以字典形式存储

#cut_text = " ".join(jieba.cut(comment_text))
d = path.dirname(__file__) # 当前文件文件夹所在目录
color_mask = imread("weibo_img.jpg") # 读取背景图片  camera.jpg\weibo_img.jpg
cloud = WordCloud(
        #设置字体，不指定就会出现乱码
        font_path="xingkai.ttf",
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=color_mask,
        #允许最大词汇
        max_words=64,
        #最大号字体
        max_font_size=400
    )
word_cloud = cloud.generate_from_frequencies(dic)# 产生词云
 #显示词云图片
image_colors = ImageColorGenerator(color_mask)
plt.imshow(word_cloud.recolor(color_func=image_colors))
word_cloud.to_file("wordcloud.jpg") #保存图片
plt.axis('off')
plt.show()








