# -*- coding: utf-8 -*-

import pandas;

data = pandas.read_csv(
    "D:\\PDM\\5.3\\data.csv"
);

dummyColumns = ["Gender", "ParentEncouragement"]

for column in dummyColumns:
    data[column]=data[column].astype('category')

dummiesData = pandas.get_dummies(
    data, 
    columns=dummyColumns,
    prefix=dummyColumns,
    prefix_sep="=",
    drop_first=True
)
dummiesData.head()
dummiesData.columns

fData = dummiesData[[
    'ParentIncome', 'IQ', 'Gender=Male',
    'ParentEncouragement=Not Encouraged'
]]

tData = dummiesData["CollegePlans"]

from sklearn.tree import DecisionTreeClassifier

dtModel = DecisionTreeClassifier(max_leaf_nodes=8)

#训练模型
dtModel.fit(fData, tData)

from sklearn.tree import export_graphviz
with open('D:\\PDM\\5.3\\data.dot','w') as f:
    f = export_graphviz(dtModel, out_file=f)

#绘图命令
#dot -Tpng data.dot -o tree.png

#安装命令
#pip install git+https://github.com/nlhepler/pydot.git
import pydot
from sklearn.externals.six import StringIO

dot_data = StringIO() 

export_graphviz(
    dtModel, 
    out_file=dot_data,
    class_names=["不计划", "计划"],
    feature_names=["父母收入", "智商", "性别=男", "父母鼓励=不鼓励"],
    filled=True, rounded=True, special_characters=True
) 

graph = pydot.graph_from_dot_data(dot_data.getvalue()) 

graph.get_node("node")[0].set_fontname("Microsoft YaHei")

graph.write_png('D:\\PDM\\5.3\\tree.png')
