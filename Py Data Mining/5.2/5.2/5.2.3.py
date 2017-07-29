# -*- coding: utf-8 -*-

import os
import codecs
import os.path

classDict = {
    'C000007': '汽车',
    'C000008': '财经',
    'C000010': 'IT',
    'C000013': '健康',
    'C000014': '体育',
    'C000016': '旅游',
    'C000020': '教育',
    'C000022': '招聘',
    'C000023': '文化',
    'C000024': '军事'
}

rootDir = "D:\\PDM\\5.2\\SogouC.mini\\Sample"

classes = [];
filePaths = [];
fileContents = [];
for c in classDict.keys():
    fileDir = os.path.join(rootDir, c)
    for root, dirs, files in os.walk(fileDir):
        for name in files:
            filePath = os.path.join(fileDir, name);
            classes.append(classDict[c]);
            filePaths.append(filePath);
            f = codecs.open(filePath, 'r', 'utf-8')
            fileContent = f.read()
            f.close()
            fileContents.append(fileContent)

import pandas;
corpos = pandas.DataFrame({
    'class': classes,
    'filePath': filePaths, 
    'fileContent': fileContents
});


import re
#匹配中文的分词
zhPattern = re.compile(u'[\u4e00-\u9fa5]+')

import jieba

segments = []
filePaths = []
for index, row in corpos.iterrows():
    segments = []
    filePath = row['filePath']
    fileContent = row['fileContent']
    segs = jieba.cut(fileContent)    
    for seg in segs:
        if zhPattern.search(seg):
            segments.append(seg)
    filePaths.append(filePath)
    row['fileContent'] = " ".join(segments);

from sklearn.feature_extraction.text import CountVectorizer

stopwords = pandas.read_csv(
    "D:\\PDM\\5.2\\StopwordsCN.txt", 
    encoding='utf8', 
    index_col=False,
    quoting=3,
    sep="\t"
)

countVectorizer = CountVectorizer(
    stop_words=list(stopwords['stopword'].values),
    min_df=0, token_pattern=r"\b\w+\b"
)
textVector = countVectorizer.fit_transform(corpos['fileContent'])

from sklearn.naive_bayes import MultinomialNB
MNBModel = MultinomialNB()

MNBModel.fit(textVector, corpos['class'])

MNBModel.score(textVector, corpos['class'])

newTexts = ["""
据介绍，EliteBook 840 G4是一款采用14英寸1080p屏幕的商务笔记本，

硬件配置方面，入门级的EliteBook 840 G4搭载Intel Core i3-7100处理器，
配备4GB内存和500GB机械硬盘，预装Windows 10操作系统。
高端机型可选择更大容量的内存和SSD固态硬盘。
机身四周提供了USB 3.0、USB-C、DisplayPort、15针迷你D-Sub，
支持蓝牙4.2和802.11ac Wi-Fi。
整机重1.48千克。
"""]

for i in range(len(newTexts)):
    newTexts[i] = " ".join(jieba.cut(newTexts[i]));

newTextVector = countVectorizer.transform(newTexts)

MNBModel.predict(newTextVector)
