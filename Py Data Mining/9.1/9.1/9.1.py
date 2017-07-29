# -*- coding: utf-8 -*-

import numpy;
import pandas;
import matplotlib.pyplot as plt;

data = pandas.read_csv('D:\\PDM\\9.1\\data.csv');

x = pandas.Series(range(1, len(data)+1))

y = data['公司A']

#SMA
Y = pandas.rolling_mean(y, 5)
plt.plot(x, y, 'k-', x, Y, 'g-')

y_ = y - Y
plt.plot(x, y_, 'r-');
plt.plot(x, y, 'k-', x, Y, 'g-', x, y_, 'r-');


#WMA
#定义窗口大小
wl = 5
#计算每个窗口值的权重
ww = numpy.arange(1, wl+1)
ww = ww/sum(ww)

def wma(window):
    return numpy.sum(window*ww);

Y = y.rolling(wl).aggregate(wma)
plt.plot(x, y, 'k-', x, Y, 'g-')

y_ = y - Y
plt.plot(x, y, 'k-', x, Y, 'g-', x, y_, 'r-');
