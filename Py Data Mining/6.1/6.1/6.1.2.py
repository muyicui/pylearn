# -*- coding: utf-8 -*-
import pandas

data = pandas.read_csv('D:\\PDM\\6.1\\data2.csv')

data['症状'] = data['症状'].astype('category')

dummiesData = pandas.get_dummies(
    data, 
    columns=['症状'],
    prefix=['症状'],
    prefix_sep="_"
)

newData = pandas.read_csv('D:\\PDM\\6.1\\data2New.csv')

dummiesNewData = pandas.get_dummies(
    newData, 
    columns=['症状'],
    prefix=['症状'],
    prefix_sep="_"
)


newData = pandas.read_csv('D:\\PDM\\6.1\\data2New.csv')

newData['症状'] = newData['症状'].astype(
    'category', 
    categories=data['症状'].cat.categories
)

dummiesNewData = pandas.get_dummies(
    newData, 
    columns=['症状'],
    prefix=['症状'],
    prefix_sep="_"
)
