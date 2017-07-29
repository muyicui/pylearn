# -*- coding: utf-8 -*-

import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

data = pandas.read_csv("D:\\PDM\\7.2\\data.csv")

eps = 0.2
MinPts = 5

model = DBSCAN(eps, MinPts)

data['type'] = model.fit_predict(data)

plt.scatter(
    data['x'], 
    data['y'],
    c=data['type']
)