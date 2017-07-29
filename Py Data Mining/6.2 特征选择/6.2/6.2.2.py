# -*- coding: utf-8 -*-

import pandas

data = pandas.read_csv('D:\\PDM\\6.2\\data2.csv')

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

selectKBest = SelectKBest(
    f_regression, k=2
)

feature = data[['月份', '季度', '广告费用', '客流量']]

bestFeature = selectKBest.fit_transform(
    feature, 
    data['销售额']
)

selectKBest.get_support()