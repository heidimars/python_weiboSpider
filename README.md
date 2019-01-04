# python_weiboSpider
代码运行说明

1.weibopr.py是用来分析大V博主影响力的，同时会爬取博主微博数据保存在weibopr这个文件夹下。

2.userid.py是用来爬取博主粉丝uid的，保存在Weibo_list_p.txt和Weibo_list_jy.txt两个文档下。

3.wb_spider.py是根据粉丝uid来爬取粉丝微博的，爬取数据分别保存在weibo_p和weibo_jy两个文件夹下，这个耗时特别久，所以我又准备了一个简易的测试代码(没在图里显示出来)，名称为wb_spider_test.py ，可以爬取10条井越的粉丝微博保存在weibo_test文件夹下。

4.LDA.py是利用LDA主题模型进行文本分析的，输出为top_words.txt和top_words2.txt两个文档，前者为彭姐的，后者为井越的。

5.cloud.py是用来生成词云图的，词云形状是根据文件夹内的背景图片。

很重要！！！说明：涉及爬取数据的代码需要本人cookie，代码中有备注提醒，不然会爬取失败。同时，在运行wb_spider.py的时候，因为爬取数据太多了，所以有可能会出现报错，只要等一会再继续运行就可以了。
