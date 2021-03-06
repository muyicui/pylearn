#Python Data Analysis笔记
'''
#Pandas.DataFrame使用
'''
import pandas as pd
import numpy as np

#创建DataFrame，用字典生成，key为列名；value为数据
df = pd.DataFrame({'A':np.arange(1,10,2),'B':np.arange(100,1000,200)})
#自定义index 
df = pd.DataFrame({'A':np.arange(1,10,2),'B':np.arange(100,1000,200)},index=['one','two','three','four','five'])

#按列搜索
df['A'];df[['A','B']]
#按行搜索，切片
df[1:3]
#行索引查看
df.loc['one'];df.loc[['one','four']]
#行列号访问
df.iloc[3:4]
#精准定位
df.at['three','B']

#查看、修改列名
df.columns#查看列名 
df.columns = ['C', 'D'] #修改列名 
#查看、修改行名
df.index
df.index = range(1,6)

#添加行信息
df.loc[len(df)] =[12, 41]
#添加列信息
df['K'] = [1.1,24,53,645674,23] 

#过滤数据，不改变df值
df.drop('C',axis=1) #axis = 1 列操作
df.drop(3,axis=0) #axis = 0 行操作

#查找
df.apply(min) #- 各列最小值，行操做
df.apply(min,axis = 1) #- 各行最小值，咧操做
df.apply(lambda x: np.all(x>0), axis =1) #- 判断所有列是否大于零

'''
#pandas.Series使用
'''
#创建Series
x = pd.Series(np.arange(0.1,1,0.3)) #默认index
x = pd.Series(np.arange(0.1,1,0.3),index=np.arange(1,4,1))# 指定index

#查看
x[1]# 支持切片

#插入
x.append(pd.Series(['1'])) #Series无法插入值，需要append序列

#查找判断
3 in x.values
x
#过滤，不改变x的值
x.drop(1) #根据index,不改变x的值
x.drop(x.index[1]) #根据位置，不改变x的值
x[0.1 != x.values]

'''
#数据导入、导出与处理
'''

#数据导入
pd.read_csv(file,encoding)
pd.read_table(file,name=[,],sep="", encoding)
pd.read_excel(fiel,sheetname,names,engine) # engine=python可以解决中文路径问题

#数据导出
pd.to_csv(filepath, sep=",", index=True, header=True) #index是否导出行索引，header是否导出列索引

#数据去重
df.duplicated() #找出行重复信息，bool值
df.duplicated(index,key) #找出列重复，根据key的值，key可以省略
df.drop_duplicates() #去重
df.drop_duplicates(index) #按列去重

#数据缺失
df.read_csv(file,na_value) #读取文件是将某个值指定为na
df.isnull() #取得是否为空的nool DataFrame
df[df.isnull()] #过滤查找NA所在行或者列
df.dropna() #去除包含na的数据行
df.fillna() #填充

#信息抽取
df[condition] #使用条件过虑信息
df[df.columns > 10] #条件比较
df[df.columns.between(10,100)] #范围比较
df.[pandas.isnull(df.columns)] #空值筛选
df.[df.title.str.contains('hello',na=False)] #信息包含

#随机抽样
df.sample(n,frac,replace=False) #n和frac设置一个即可

#记录合并
concat([df1,df2])

#字段匹配
merge（df1,df2,left_on, right_on,how) #how:left,right,inner,outer

#数值计算
df.extra_column = #并不咋df中添加数据列
df['extra_column'] #结果将加入df中

#数据标准化， 将数据0~1标准化
df.data.min() #最小值
df.data.max()#最大值

#数据分组
cut(series,bins,right=True,lables=NULL) #bin为分组列表 min()-1 ~ max()+1 

#时间处理
pandas.to_datetime(df.datestring,format) #%Y,%m,%d,%H,%M,%S
df.dt.strftime(format)
df.datetime.dt.property #property = year, month, day, hour, minute,second

#时间抽取
df.ix[start:end]
df.ix[dates]

#虚拟变量 大小关系 如Ｍ，Ｌ，ＸＬ；没有大小意义　如Ｒed Blue
pandas.Series.map(dict)#有大小关系
pandas.get_dummies(data,prefix=None,prefix_sep=' ',dummy_na=False,columns=None, drop_first=False )

