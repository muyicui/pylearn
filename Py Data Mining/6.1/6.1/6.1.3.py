# -*- coding: utf-8 -*-
import pandas

data = pandas.read_csv('D:\\PDM\\6.1\\data3.csv')

from sklearn.preprocessing import Imputer;

#'mean', 'median', 'most_frequent'
imputer = Imputer(strategy='mean')

imputer.fit_transform(data[['累计票房']])
