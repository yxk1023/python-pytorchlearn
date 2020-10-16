import numpy as np

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# def f(x):
#     return x*x
# r = map(f,[1,2,3,4,5])
# print(r)
# print(list(r))
#
# l = []
# for x in range(1,6):
#     l.append(f(x))
# print(l)
#
# print(list(map(str,[1,2,3,4,5,6,7,8,9,10])))    #把这个list所有数字转为字符串：

from functools import reduce            #reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
                                        # 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# def add(x,y):
#     return x+y
# print(reduce(add,[1,2,3,4]))
#
# def fn(x,y):
#     return 10*x+y
# print(reduce(fn,[1,2,3,4,5,6,7,8,9]))
#
# def char2num(s):
#     digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]
#
# q = reduce(fn,map(char2num,'567234'))
# print(q)

#整理成一个str2int的函数就是：
# digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str2int(s):
#     def fn(m,n):
#         return 10*m+n
#     def fn2(k):
#         return digits[k]
#     return reduce(fn,map(fn2,s))
# print(str2int('78963'))

