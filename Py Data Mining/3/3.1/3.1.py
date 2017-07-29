import numpy

X = [
    12.5, 15.3, 23.2, 26.4, 33.5, 
    34.4, 39.4, 45.2, 55.4, 60.9
]
Y = [
    21.2, 23.9, 32.9, 34.1, 42.5, 
    43.2, 49.0, 52.8, 59.4, 63.5
]

#均值
XMean = numpy.mean(X);
YMean = numpy.mean(Y);

#标准差
XSD = numpy.std(X);
YSD = numpy.std(Y);

#z分数
ZX = (X-XMean)/XSD;
ZY = (Y-YMean)/YSD;

#相关系数
r = numpy.sum(ZX*ZY)/(len(X));
r
#直接调用Python的内置的方法计算
numpy.corrcoef(X, Y)

import pandas;

data = pandas.DataFrame({
    'X': X, 
    'Y': Y
})
data.corr()