# -*- coding: utf-8 -*-

import pandas;
from pandas import read_csv;

data = read_csv(
    'D:\\PDM\\4.4\\data.csv', 
    encoding='utf8'
)
data = data.dropna()

data.shape

dummyColumns = [
    'Gender', 'Home Ownership', 
    'Internet Connection', 'Marital Status',
    'Movie Selector', 'Prerec Format', 'TV Signal'
]

for column in dummyColumns:
    data[column]=data[column].astype('category')

dummiesData = pandas.get_dummies(
    data, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep=" ",
    drop_first=True
)

data.Gender.unique()

dummiesData.columns

"""
博士后    Post-Doc
博士      Doctorate
硕士      Master's Degree
学士      Bachelor's Degree
副学士    Associate's Degree
专业院校  Some College
职业学校  Trade School
高中      High School
小学      Grade School
"""
educationLevelDict = {
    'Post-Doc': 9,
    'Doctorate': 8,
    'Master\'s Degree': 7,
    'Bachelor\'s Degree': 6,
    'Associate\'s Degree': 5,
    'Some College': 4,
    'Trade School': 3,
    'High School': 2,
    'Grade School': 1
}

dummiesData['Education Level Map'] = dummiesData['Education Level'].map(educationLevelDict)

freqMap = {
    'Never': 0,
    'Rarely': 1,
    'Monthly': 2,
    'Weekly': 3,
    'Daily': 4
}
dummiesData['PPV Freq Map'] = dummiesData['PPV Freq'].map(freqMap)
dummiesData['Theater Freq Map'] = dummiesData['Theater Freq'].map(freqMap)
dummiesData['TV Movie Freq Map'] = dummiesData['TV Movie Freq'].map(freqMap)
dummiesData['Prerec Buying Freq Map'] = dummiesData['Prerec Buying Freq'].map(freqMap)
dummiesData['Prerec Renting Freq Map'] = dummiesData['Prerec Renting Freq'].map(freqMap)
dummiesData['Prerec Viewing Freq Map'] = dummiesData['Prerec Viewing Freq'].map(freqMap)

dummiesData.columns


dummiesSelect = [
    'Age', 'Num Bathrooms', 'Num Bedrooms', 'Num Cars', 'Num Children', 'Num TVs', 
    'Education Level Map', 'PPV Freq Map', 'Theater Freq Map', 'TV Movie Freq Map', 
    'Prerec Buying Freq Map', 'Prerec Renting Freq Map', 'Prerec Viewing Freq Map', 
    'Gender Male',
    'Internet Connection DSL', 'Internet Connection Dial-Up', 
    'Internet Connection IDSN', 'Internet Connection No Internet Connection',
    'Internet Connection Other', 
    'Marital Status Married', 'Marital Status Never Married', 
    'Marital Status Other', 'Marital Status Separated', 
    'Movie Selector Me', 'Movie Selector Other', 'Movie Selector Spouse/Partner', 
    'Prerec Format DVD', 'Prerec Format Laserdisk', 'Prerec Format Other', 
    'Prerec Format VHS', 'Prerec Format Video CD', 
    'TV Signal Analog antennae', 'TV Signal Cable', 
    'TV Signal Digital Satellite', 'TV Signal Don\'t watch TV'
]

inputData = dummiesData[dummiesSelect]

outputData = dummiesData[['Home Ownership Rent']]

from sklearn import linear_model

lrModel = linear_model.LogisticRegression()

lrModel.fit(inputData, outputData)

lrModel.score(inputData, outputData)

newData = read_csv(
    'D:\\PDM\\4.4\\newData.csv', 
    encoding='utf8'
)

for column in dummyColumns:
    newData[column] = newData[column].astype(
        'category', 
        categories=data[column].cat.categories
    )

newData = newData.dropna()

newData['Education Level Map'] = newData['Education Level'].map(educationLevelDict)
newData['PPV Freq Map'] = newData['PPV Freq'].map(freqMap)
newData['Theater Freq Map'] = newData['Theater Freq'].map(freqMap)
newData['TV Movie Freq Map'] = newData['TV Movie Freq'].map(freqMap)
newData['Prerec Buying Freq Map'] = newData['Prerec Buying Freq'].map(freqMap)
newData['Prerec Renting Freq Map'] = newData['Prerec Renting Freq'].map(freqMap)
newData['Prerec Viewing Freq Map'] = newData['Prerec Viewing Freq'].map(freqMap)

dummiesNewData = pandas.get_dummies(
    newData, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep=" ",
    drop_first=True
)

inputNewData = dummiesNewData[dummiesSelect]

lrModel.predict(inputData)
