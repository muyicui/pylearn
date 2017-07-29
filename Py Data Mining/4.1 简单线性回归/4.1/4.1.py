
import numpy;
from pandas import read_csv;
from matplotlib import pyplot as plt;
from sklearn.linear_model import LinearRegression

data = read_csv(
    'D:\\PDM\\4.1\\data.csv'
)

#第二步，画出散点图，求x和y的相关系数
plt.scatter(data.广告投入, data.销售额)

data.corr()

#第三步，估计模型参数，建立回归模型
lrModel = LinearRegression()

x = data[['广告投入']]
y = data[['销售额']]

#训练模型
lrModel.fit(x, y)

#第四步、对回归模型进行检验
lrModel.score(x, y)

#第五步、利用回归模型进行预测
lrModel.predict([[50], [40], [30]])

#查看截距
alpha = lrModel.intercept_[0]

#查看参数
beta = lrModel.coef_[0][0]

alpha + beta*numpy.array([50, 40, 30])
