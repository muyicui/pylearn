# -*- coding: utf-8 -*-

import pandas;

data = pandas.read_csv(
    "D:\\PDM\\5.3\\data.csv"
);

dummyColumns = ["Gender", "ParentEncouragement"]

for column in dummyColumns:
    data[column]=data[column].astype('category')

dummiesData = pandas.get_dummies(
    data, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep="=",
    drop_first=True
)
dummiesData.columns

fData = dummiesData[[
    'ParentIncome', 'IQ', 'Gender=Male',
    'ParentEncouragement=Not Encouraged'
]]

tData = dummiesData["CollegePlans"]

from sklearn.tree import DecisionTreeClassifier

dtModel = DecisionTreeClassifier(max_leaf_nodes=8)

from sklearn.model_selection import cross_val_score

cross_val_score(
    dtModel, 
    fData, tData, cv=10
)
