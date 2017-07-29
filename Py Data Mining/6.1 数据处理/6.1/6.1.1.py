# -*- coding: utf-8 -*-

import pandas

data = pandas.read_csv('D:\\PDM\\6.1\\data1.csv')

#Min-Max标准化
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

data['标准化累计票房'] = scaler.fit_transform(data['累计票房'])
data['标准化豆瓣评分'] = scaler.fit_transform(data['豆瓣评分'])

#Z-Score标准化
from sklearn.preprocessing import scale

data['标准化累计票房'] = scale(data['累计票房'])
data['标准化豆瓣评分'] = scale(data['豆瓣评分'])

#Normalizer归一化
from sklearn.preprocessing import Normalizer

scaler = Normalizer()

data['归一化累计票房'] = scaler.fit_transform(
    data['累计票房']
)[0]
data['归一化豆瓣评分'] = scaler.fit_transform(
    data['豆瓣评分']
)[0]

