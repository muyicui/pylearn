# -*- coding: utf-8 -*-

import pandas
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('D:\\PDM\\6.2\\data2.csv')

feature = data[['月份', '季度', '广告费用', '客流量']]

rfe = RFE(
    estimator=LinearRegression(), 
    n_features_to_select=2
)

sFeature = rfe.fit_transform(
    feature, 
    data['销售额']
)

rfe.get_support()

