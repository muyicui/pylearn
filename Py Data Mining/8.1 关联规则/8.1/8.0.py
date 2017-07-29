# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 16:42:33 2016

@author: manfang
"""
import numpy
import pandas
from itertools import combinations

data = pandas.read_csv('D:\\PDM\\7.1\\data.csv')

goods = numpy.unique(data['购买商品'])
goodsCount = numpy.unique(data['购买商品']).size
recodeCount = numpy.unique(data['交易ID']).size

goodsStat = data.pivot_table(
    index='交易ID', 
    columns='购买商品',
    aggfunc=len
)

del goodsStat.columns.name
del goodsStat.index.name

minTimes = 2

rules = []
supports = []
confidences = []
lifts = []

#遍历项出现的次数，从1项式开始，到所有商品个数的项式
for times in range(1, goodsCount):
    #从所有的商品中，挑出项式的符合模式，然后遍历所有的组合模式
    for cols in combinations(goods, times):
        #如果同时出现的次数大于 minTimes，那么才继续进行 支持度，置信度的计算
        if sum(goodsStat[list(cols)].sum(axis=1)==len(cols))>=minTimes:
            #开始计算互相之间的推导的支持度与置信度
            for col in combinations(cols, 1):
                #获取推导的项
                _cols = list(set(cols)-set(col))
                
                subRecodeCount = sum(goodsStat[list(_cols)].sum(axis=1)==len(_cols))

                #生成规则
                rule = ','.join(list(_cols)) + " -> " + ','.join(list(col))
                rules.append(rule)
                support = sum(goodsStat[list(cols)].sum(axis=1)==len(cols))/recodeCount
                supports.append(support)
                confidence = sum(goodsStat[list(cols)].sum(axis=1)==len(cols))/subRecodeCount
                confidences.append(confidence)
                lifts.append(confidence/support)
                
result = pandas.DataFrame({
    'rule': rules, 
    'supports': supports, 
    'confidence': confidences, 
    'lift':lifts
})
