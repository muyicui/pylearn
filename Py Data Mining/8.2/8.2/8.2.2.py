# -*- coding: utf-8 -*-

import numpy
import pandas
from sklearn.metrics.pairwise import euclidean_distances

data = pandas.read_csv('D://PDM//8.2//data.csv')

#生成评分-用户矩阵
userRating = data.pivot_table(
    index='ItemID', 
    columns='UserID',
    aggfunc=sum,
    fill_value=0
)

#将透视表转为数据框，主要是整理列格式
userRating.columns = userRating.columns.droplevel(0)
del userRating.columns.name

#计算每个物品之间的距离
dist = pandas.DataFrame(euclidean_distances(userRating))
dist.index = userRating.index
dist.columns = userRating.index

#计算每个商品之间的相似度
sim = 1/(1+dist)

#用户ID
userId = 3

userItems = userRating[3]

#根据用户的评分和相似度矩阵，计算出每种物品的得分
score = pandas.DataFrame(
    numpy.dot(
        userItems, sim
    )
)

#对结果排序，得到最终的结果
result = userRating.index[
    score.sort(0, ascending=False).index
]
