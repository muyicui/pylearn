# -*- coding: utf-8 -*-

from sklearn import svm
from sklearn import datasets

SVMModel = svm.SVC()

iris = datasets.load_iris()

X, y = iris.data, iris.target

SVMModel.fit(X, y)  

from sklearn.externals import joblib

joblib.dump(
    SVMModel, 
    'D:\\PDM\\10\\SVMModel.sklearn'
)

#到这里，关闭console，重新启动一个console

from sklearn.externals import joblib

SVMModel = joblib.load(
    'D:\\PDM\\10\\SVMModel.sklearn'
)

from sklearn import datasets

iris = datasets.load_iris()

X, y = iris.data, iris.target

SVMModel.score(X, y)

Y = SVMModel.predict(X)

import pandas

pandas.crosstab(y, Y)