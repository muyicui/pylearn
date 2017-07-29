# -*- coding: utf-8 -*-

import numpy
import pandas
import matplotlib.pyplot as plt

#导入数据
data = pandas.read_csv("D:\\PDM\\7.2\\data.csv")

plt.scatter(
    data['x'], 
    data['y']
)

eps = 0.2
MinPts = 5

from sklearn.metrics.pairwise import euclidean_distances

dist = euclidean_distances(data)

ptses = []

for row in dist:
    #密度,空间中任意一点的密度是以该点为圆心、以 Eps 为半径的圆区域内包含的点数
    density = numpy.sum(row<eps)
    pts = 0;
    if density>MinPts:
        #核心点（Core Points）
        #空间中某一点的密度，如果大于某一给定阈值MinPts，则称该为核心点
        pts = 1
    elif density>1 :
        #边界点（Border Points）
        #空间中某一点的密度，如果小于某一给定阈值MinPts，则称该为边界点
        pts = 2
    else:
        #噪声点（Noise Points）
        #数据集中不属于核心点，也不属于边界点的点，也就是密度值为1的点
        pts = 0
    ptses.append(pts)

#把噪声点过滤掉，因为噪声点无法聚类，它们独自一类
corePoints = data[pandas.Series(ptses)!=0]

coreDist = euclidean_distances(corePoints)

#首先，把每个点的领域都作为一类
#邻域（Neighborhood）
#空间中任意一点的邻域是以该点为圆心、以 Eps 为半径的圆区域内包含的点集合
cluster = dict();
i = 0;
for row in coreDist: 
    cluster[i] = numpy.where(row<eps)[0]
    i = i + 1

#然后，将有交集的领域，都合并为新的领域
for i in range(len(cluster)):
    for j in range(len(cluster)):
        if len(set(cluster[j]) & set(cluster[i]))>0 and i!=j:
            cluster[i] = list(set(cluster[i]) | set(cluster[j]))
            cluster[j] = list();

#最后，找出独立（也就是没有交集）的领域，就是我们最后的聚类的结果了
result = dict();
j = 0
for i in range(len(cluster)):
  if len(cluster[i])>0:
    result[j] = cluster[i]
    j = j + 1

#找出每个点所在领域的序号，作为他们最后聚类的结果标记
for i in range(len(result)):
    for j in result[i]:
        data.at[j, 'type'] = i
 
plt.scatter(
    data['x'], 
    data['y'],
    c=data['type']
)