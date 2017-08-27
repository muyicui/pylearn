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
