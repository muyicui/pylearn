# -*- coding: utf-8 -*-

import numpy
import pandas
from sklearn.metrics.pairwise import euclidean_distances

data = pandas.read_csv(
    'D://PDM//8.2//data.csv'
)

#生成用户-评分矩阵
userRating = data.pivot_table(
    index='UserID', 
    columns='ItemID',
    aggfunc=sum,
    fill_value=0
)

#将透视表转为数据框，主要是整理列格式
userRating.columns = userRating.columns.droplevel(0)
del userRating.columns.name

#计算每个用户之间的距离
dist = pandas.DataFrame(
    euclidean_distances(userRating)
)
dist.index = userRating.index
dist.columns = userRating.index

#计算每个用户之间的相似度
sim = 1/(1+dist)

#邻居个数
k = 3
#用户ID
userId = 3

#获取相似用户
simUserIds = sim.sort(
    userId, ascending=False
)[userId].index[1:k+1]

simUser = sim.ix[simUserIds, userId]

#根据相似用户，计算出每个物品的评分
score = pandas.DataFrame(
    numpy.dot(
        simUser, 
        userRating.ix[simUserIds]
    )
)

#对结果排序，得到最终的结果
result = userRating.columns[
    score.sort(
        0, ascending=False
    ).index.values
]
