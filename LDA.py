# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 21:55:58 2018

@author: Administrator
"""

from nltk.tokenize import RegexpTokenizer
#from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
#import jieba
import codecs
import numpy as np
from multiprocessing import cpu_count
from gensim.models import TfidfModel, LdaMulticore
#import sys
import csv


tokenizer = RegexpTokenizer(r'\w+')


stopwords = [stopwords[:-1] for stopwords in codecs.open('stop_words.txt', encoding='utf8', mode='r')]
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

list1=[]   
txt_list = os.listdir('weibo_jy')#   folder_path为此时文件路径          lisidir 获取路径中的文件夹中的每个文件           
for t in txt_list:#遍历里面每个文件
    new_folder_path = os.path.join('weibo_jy', t)        #根据子文件夹，生成新的路径   path.join 为前面的folder_path+后面的folder  例如：C:\CHE\+ 1.txt = C:\CHE\1.txt  即遍历后获取每个txt文件的绝对路径                   
    f = open(new_folder_path, 'r', encoding='utf-8')  #打开改路径的文件 ‘r’为read读的意思 ‘w’为写  后面是编码
    try:
        next(f)
        list1.extend(f.readlines())#读取信息即可
        print(len(list1))
    except StopIteration:
        print('StopIteration')    

texts = []
a=0
# 遍历每个文件
for i in list1[0:30000]:
    
    # 数据清理 
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # 清除包含在停用词文档中的词语
    stopped_tokens = [i for i in tokens if not i in stopwords]    
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]    
    texts.append(stemmed_tokens)
    a=a+1
    #print(a)

# 将文档转化为字典
dictionary = corpora.Dictionary(texts)
print('-1')    
#转化成文档矩阵
corpus = [dictionary.doc2bow(text) for text in texts]
print('0')
#生成LDA模型
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=100, id2word = dictionary, passes=200)
print('1')
topics = []
for doc in corpus:
	topics.append(ldamodel[doc])
print('2')

counts = np.zeros(100)
for top_doc in topics:
	for ti, _ in top_doc:
		counts[ti] += 1
print('3')

words = ldamodel.show_topic(counts.argmax(), 64)
print(type(words))
data = list(map(lambda x:[x],words))
try:    
    with open('top_words2.txt', 'w', newline='') as tw:
        writer = csv.writer(tw)
        for i in data:
            writer.writerows(i)
    print('4')
except Exception as e:  
    print("Write an CSV file to path: %s, Case: %s" % (e)) 

print(ldamodel.print_topics(num_topics=10, num_words=10))
print(ldamodel.print_topics(num_topics=5, num_words=10))
print(ldamodel.print_topics(num_topics=10, num_words=5))

