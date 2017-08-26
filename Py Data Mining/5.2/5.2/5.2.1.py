# -*- coding: utf-8 -*-

import pandas;

data = pandas.read_csv(
    'D:\\PDM\\5.2\\data1.csv', 
    encoding='utf8'
)

dummyColumns = ['症状', '职业']

for column in dummyColumns:
    data[column]=data[column].astype('category')

dummiesData = pandas.get_dummies(
    data, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep=" "
)

dummiesData = pandas.get_dummies(
    data, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep=" ",
    drop_first=True
)

#伯努利贝叶斯
from sklearn.naive_bayes import BernoulliNB
BNBModel = BernoulliNB()

fNames = ['症状 打喷嚏', '职业 建筑工人', '职业 护士', '职业 教师']
tData = dummiesData['疾病']
fData = dummiesData[fNames]

BNBModel.fit(fData, tData)

#病症是打喷嚏的建筑工人
newData = pandas.DataFrame({
    '症状':['打喷嚏'],
    '职业':['建筑工人']
})

for column in dummyColumns:
    newData[column] = newData[column].astype(
        'category', 
        categories=data[column].cat.categories
    )

dummiesNewData = pandas.get_dummies(
    newData, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep=" ",
    drop_first=True
)

pData = dummiesNewData[fNames]
BNBModel.predict(pData)