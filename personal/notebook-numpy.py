#Python Data Analysis笔记
'''
#numpy使用
'''
import numpy as np

#使用arrange创建列表, start[,end),diff
r = np.arange(1, 10, 2)

#基本运算
r+r; r-r; r*r; r/r

#power 乘幂
np.power(r,5) 

#向量判断及过滤
r>3
r[r>3]

#矩阵运算（待更新）
np.dot(r,r.T)
