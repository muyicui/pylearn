# -*- coding: utf-8 -*-

import pandas
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import SelectFromModel

data = pandas.read_csv('D:\\PDM\\6.2\\data2.csv')

feature = data[['月份', '季度', '广告费用', '客流量']]

lrModel = LinearRegression()

selectFromModel = SelectFromModel(lrModel)

selectFromModel.fit_transform(
    feature, 
    data['销售额']
)

feature.columns[selectFromModel.get_support()]
