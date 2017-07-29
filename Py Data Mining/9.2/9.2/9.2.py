# -*- coding: utf-8 -*-

import pandas

import statsmodels.api as sm

data = pandas.read_csv(
    'D:\\PDM\\9.2\\data.csv'
)

dateparse = lambda dates: pandas.datetime.strptime(
    dates, '%Y%m%d'
)

data = pandas.read_csv(
    'D:\\PDM\\9.2\\data.csv',
    parse_dates=['时间'],
    date_parser=dateparse, 
    index_col='时间'
)

rd = sm.tsa.seasonal_decompose(
    data['总销量'].values, 
    freq=7
)

resplot = rd.plot()

rd.trend
rd.seasonal
rd.resid
