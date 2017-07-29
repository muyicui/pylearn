# -*- coding: utf-8 -*-
'''
#Created on Sat Jul 29 21:58:52 2017
#@author: Muyi
#for python strip
'''

i = 'abcde hig'
#处理空格
i.str.strip()
i.str.lstrip()
i.str.rstrip()

#字符串拆分
i.split(' ')[0] #使用空格拆分， 返回列表