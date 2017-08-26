# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 22:01:41 2017

@author: Muyi
notebook for lib os
"""
import os 

 os.listdir(path) #遍历中文件，返回array
 os.rename(old, new) #修改文件名

#os.path
 os.path.isdir(path)  #目标是否为文件夹，bool
 os.path.join(path,filename) #生成绝对路径