# -*- coding: utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as hcluster

data = pandas.read_csv('D:\\PDM\\7.1\\data.csv')

fColumns = [
    '工作日上班时电话时长', '工作日下半时电话时长', 
    '周末电话时长', '国际电话时长', '平均每次通话时长'
]

linkage = hcluster.linkage(
    data[fColumns], 
    method='centroid'
)

hcluster.dendrogram(
    linkage
)

hcluster.dendrogram(
    linkage,
    truncate_mode='lastp', 
    p=12,    
    leaf_font_size=12.
)

pTarget = hcluster.fcluster(
    linkage, 3, 
    criterion='maxclust'
)

pandas.crosstab(pTarget, pTarget)

pca_2 = PCA(n_components=2)
data_pca_2 = pandas.DataFrame(
    pca_2.fit_transform(data[fColumns])
)

plt.scatter(
    data_pca_2[0], 
    data_pca_2[1],
    c=pTarget
)

dMean = pandas.DataFrame(columns=fColumns+['分类'])
data_gb = data[fColumns].groupby(pTarget)
i = 0;
for g in data_gb.groups:
    rMean = data_gb.get_group(g).mean()
    rMean['分类'] = g;
    dMean = dMean.append(rMean, ignore_index=True)
    subData = data_gb.get_group(g)
    for column in fColumns:
        i = i+1;
        p = plt.subplot(3, 5, i)
        p.set_title(column)
        p.set_ylabel(str(g) + "分类")
        plt.hist(subData[column], bins=20)
