import pandas
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()

data = iris.data
target = iris.target

pca_3 = PCA(n_components=3)
data_pca_3 = pca_3.fit_transform(data)

"""
散点样式：

参数	样式
'.'	实心点
'o'	圆圈
','	一个像素点
'x'	叉号
'+'	十字
'*'	星号
'^' 'v' '<' '>'	三角形(上下左右)
'1' '2' '3' '4'	三叉号（上下左右）

颜色：

参数	颜色
'b'	蓝
'g'	绿
'r'	红
'c'	青
'm'	品红
'y'	黄
'k'	黑
'w'	白
"""
colors = {
    0: 'r',
    1: 'b',
    2: 'k'
}

markers = {
    0: 'x',
    1: 'D',
    2: 'o'
}

#弹出图形
#%matplotlib qt

#三维数据
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)

data_pca_gb = pandas.DataFrame(
    data_pca_3
).groupby(target)

for g in data_pca_gb.groups:
    ax.scatter(
        data_pca_gb.get_group(g)[0], 
        data_pca_gb.get_group(g)[1], 
        data_pca_gb.get_group(g)[2], 
        c=colors[g], 
        marker=markers[g],
        cmap=plt.cm.Paired
    )

#二维数据
pca_2 = PCA(n_components=2)
data_pca_2 = pca_2.fit_transform(data)

data_pca_gb = pandas.DataFrame(data_pca_2).groupby(target)

import matplotlib.pyplot as plt;

for g in data_pca_gb.groups:
    plt.scatter(
        data_pca_gb.get_group(g)[0], 
        data_pca_gb.get_group(g)[1], 
        c=colors[g], 
        marker=markers[g]
    )

