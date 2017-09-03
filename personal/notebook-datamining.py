# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:28:53 2017

@author: Muyi
"""
import numpy as np
import pandas as pd
df = pd.DataFrame({'A':np.arange(1,10,2),'B':np.arange(100,1000,200)})

#变量
a = 1       #数值整形
a = '1'     #字符类型
a = 'abc'   #字符串
a = True    #布尔值

#数据类型
#Logical 布尔型 用于比较
    #运算符 & | not
    #数据值 True False
#Numeric
    #实数 
    #运算 +，-，*。/
#Character
    #所有可定义字符
    #表示： '',"",''' '''

#数据结构
    #学习方法: 概念，定义，限制，访问，修改
    #pandas.Series
    #pandas.DataFrame

#向量运算
np.arrange(start,end,step)
    #向量计算原则：避免使用for，不要过早优化

#数据导入导出
#导入
pd.read_csv(file,encoding)
pd.read_table(file, columnname,sep="",encoding)
pd.read_excel(file,sheetname,columname)
#导出
df.to_csv(filePath, sep="",index = True, header = True)

#-------------------------------------------------------------#
#语料库Corpus， 分析所以内容的集合
#1. 整理语料库，生成路径列表->读取数据至数组->生成DataFrame
import codecs
codecs.open(path,'r','utf-8')

#中文分词，需要分词工具
#安装jieba， pip install jieba

import jieba
for w in jieba.cut("我爱吃饺子") #分词案例
jieba.add_word("不分词") #添加词库
jieba.load_userdict(path) #添加词库

#文本挖掘 1。 词频统计
#对分词结果进行统计分析，发现高频词
#去除停用词，设置stopword

#词云图绘制 Word Cloud 
from wordcloud iport WordCloud
import matplotlib.pyplot as plt

wd = WordCloud(font_path,background_color)
plt.imshow(wd)
plt.close()


