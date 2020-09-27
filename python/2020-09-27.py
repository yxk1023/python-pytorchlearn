import numpy as np
import torch
import math
import matplotlib.pyplot
import os
#列表生成式

# l = [x*x for x in range(1,10,2)]
# print(l)
# x = [x*x for x in range(1,11) if x%2 ==0]
# print(x)
# n = [p+q for p in 'ABC' for q in str(123)]
# print(n)

# d = [d for d in os.listdir()]
# print(d)
# a = [a for a in os.listdir('.')]
# print(a)

# d = {'A':1 ,'B':2,'C':3}
# for i ,j in d.items():
#     print(i,'=',j)                          #这里输出打印是用逗号分隔开输出
#
# m = {'x':'111','y':'222','z':'333'}
# l = [j +'='+k for j,k in m.items()]         #这里列表生成式里面是字符串拼接一个数组中的元素，然后生成一个列表
# print(l)
#
# L = ['ADC','SUP','TOP','MID','JUG']
# x = [c.lower() for c in L]                  #lower()是把字符串变成小写样式
# print(x)


m = [m*m for m in range(1,11) if m%2 == 0]
x = [x*x if x%2 ==0 else -x for x in range(1,11) ]
print(m,'\n',x)
#可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
