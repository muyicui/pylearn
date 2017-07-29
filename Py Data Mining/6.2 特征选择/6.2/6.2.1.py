# -*- coding: utf-8 -*-

import pandas

data = pandas.read_csv('D:\\PDM\\6.2\\data1.csv')

from sklearn.feature_selection import VarianceThreshold

varianceThreshold = VarianceThreshold(threshold=1)

varianceThreshold.fit_transform(data[['累计票房', '豆瓣评分']])

data[['累计票房', '豆瓣评分']].std()

varianceThreshold = VarianceThreshold(threshold=3)

varianceThreshold.fit_transform(data[['累计票房', '豆瓣评分']])

varianceThreshold.get_support()