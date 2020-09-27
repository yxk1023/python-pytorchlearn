import math
import torch
import numpy as np
import matplotlib.pyplot
#
# def power (x):
#     return x*x
# print(power(2))

#默认参数的应用
# def power (x,n=2):
#     mul = 1
#     i = 1
#     for i in range(1,n+1):
#         mul = mul *x
#     return mul
#
# print(power(3))

# def add_end (l=None):
#     if l == None:
#         l = []
#     l.append('end')
#     return l
#
# print(add_end([1,2,3]))
# print(add_end(['2',2,'aa']))
# print(add_end())
# print(add_end())

#可变长度的参数调用
# def calculater (*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i *i
#     return sum
# a = [1,2,3]
# print(calculater(*a))

# def person (name ,age ,**kw):
#     print('name:',name,'age:',age,'\nothers:',kw)
#
# print(person('ye',12,city='shanghai',hu='sss',assdadsd=1))
#
# a = {'s':1,'2':'sd'}
# print(a)

# def guanjianzi (name ,age ,*fw,city='beijing',job):
#     print(name,age,city,job)
# guanjianzi('ye',22,job='student')


#参数组合
def f1 (a ,b ,c = 0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
def f2 (a ,b ,c = 0,*,city,**kw):
    print('a=',a,'b=',b,'c=',c,city,'kw=',kw)
def f3 (a ,b ,c = 0,*x,city,**kw):
    print('a=',a,'b=',b,'c=',c,'x=',x,'city=',city,'kw=',kw)


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# f1(2222,1111)
# f1(11,22,33,'2',12,233)
# f1(1,2,3,[1,2],wp='ni',caa='ta')
# f1(12,22,2,2,2,2,2,2,2,2,2,x=22,y=222,z=222222)
#
# f3(1,2,3,4,4,4,city=1,f=1,xxx=111)
# f3(2,3,4,5,5,6,6,6,6,s2='112,',s3 = 's1',city=1)
#
# args = [1,2,3,4]
# fw = {'city':111,';;;':112}     #所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
# f3(*args,**fw)
# a=[1,2]
# print(len(a))

#小结：Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。
# 以及调用函数时如何传入可变参数和关键字参数的语法：
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。

#递归
# def jiecheng (n):
#     if n==1:
#         return 1
#     return n*jiecheng(n-1)
# print(jiecheng(5))

#汉诺塔的递归问题 有点难 慢慢理解

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
# move(3,'A','B','C')
#
# L = []
# for i in range(1,100,2):
#     L.append(i)
# print(L)
# print(L[:len(L)//2])
# print(L[0:3])  #切片
# print(L[:2])
# print(L[-10:])
# print(L[10:20])
# print(L[1:10:2])
# print(L[::5])
# print(L[:])
# print((1,2,3,4,5)[:2])
# print('abcdefghijklmnopqrsuvwxyz'[::5])


#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
# def trim(s):
#     for i in s:
#         if i ==' ':
#             s = s[1:]
#         else:break
#     n = len(s)
#     for j in range(n-1,1,-1):
#         if s[j]==' ':
#             s = s[:-1]
#         else:break
#     return s
#
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# dict = {'name':'yexiekang','age':23,'family':'wang'}
# for i in dict:
#     print(i)
# for value in dict.values():   #得到dict的value值
#     print(value)
# for k,v in dict.items():        #得到dict的key value值
#     print(k,v)
# for i in 'ABC':
#     print(i)

# from collections import Iterable
# print(isinstance('ABC',Iterable))
# print(isinstance(['123'],Iterable))
# print(isinstance(123,Iterable))

# for i ,j in enumerate(['a','b','c']):
#     print(i,j)
#
# for x,y in [(1,1),(2,2)]:
#     print(x,y)


#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     min=L[0]
#     max=L[0]
#     for x in L[1:]:
#         if x>max:
#             max=x
#         if x<min:
#             min = x
#     return min , max
#
# # 测试
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')

