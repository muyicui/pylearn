# -*- coding: utf-8 -*-

import scipy.io as scio

wineData = scio.loadmat('D:\\PDM\\5.5\\data.mat')

wineData['categories']

fData = wineData['wine']
tData = wineData['wine_labels'].reshape(-1)

from sklearn import svm
from sklearn import cross_validation;

svmModel = svm.SVC()
cross_validation.cross_val_score(
    svmModel, 
    fData, tData, cv=3
)

svmModel = svm.NuSVC()
cross_validation.cross_val_score(
    svmModel, 
    fData, tData, cv=3
)

svmModel = svm.LinearSVC()
cross_validation.cross_val_score(
    svmModel, 
    fData, tData, cv=3
)

svmModel = svm.LinearSVC()
svmModel.fit(fData, tData)
svmModel.score(fData, tData)
