# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:11:04 2017

@author: Muyi
self created lib, copy to lib root directory
"""

import os 

path_da = "C:\\Users\\Muyi\\PycharmProjects\\pylearn\\Py Data Analysis"
path_dm = "C:\\Users\\Muyi\\PycharmProjects\\pylearn\\Py Data Mining"

def findpath_da(input):
    return os.path.join(path_da,input)

def findpath_dm(input):
    return os.path.join(path_dm,input)