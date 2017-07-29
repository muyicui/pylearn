# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:42:37 2017

@author: fangx
"""

import pandas;

data = pandas.read_csv(
    'D:\\PDM\\5.2\\data2.csv', 
    encoding='utf8'
)

mean = data[data.性别=='男']['身高（英尺）'].mean()
std = data[data.性别=='男']['身高（英尺）'].std()

from scipy.stats import norm
norm.pdf(6, mean, std)
