import os
import os.path
import re
import shutil


root = "C:\\Users\\muyicui\\PycharmProjects\\pylearn"
data_Analysis = root+"\\Py Data Analysis"
data_Mining = root+"\\Py Data Mining"

##list dirnames in txt
'''
analysis = open(data_Analysis+"\\text.txt",'w')
mining = open(data_Mining+"\\text.txt",'w')
for i in os.listdir(data_Analysis):
    analysis.write(os.path.basename(i)+'\n')
for i in os.listdir(data_Mining):
    mining.write(os.path.basename(i)+'\n')
analysis.close()
mining.close()
'''

##change dir names
'''
filelist = os.listdir(data_Analysis)
for i in filelist:
    if os.path.isdir(os.path.join(data_Analysis,i)):
        os.rename(os.path.join(data_Analysis,i),os.path.join(data_Analysis,i.split(' ')[0]))

filelist = os.listdir(data_Mining)
for i in filelist:
    if os.path.isdir(os.path.join(data_Mining,i)):
        os.rename(os.path.join(data_Mining,i),os.path.join(data_Mining,i.split(' ')[0]))
'''
##didn't finish
filelist = os.listdir(data_Analysis)
print(filelist)
for i in filelist:
    if os.path.isdir(os.path.join(data_Analysis,i)):
        src = os.path.join(data_Analysis,i)
        dst = os.path.join(src,os.listdir(src)[0])
##
print(src)
print(dst)
##shutil.copy(dst,src)