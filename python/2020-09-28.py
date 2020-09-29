import numpy as np
import torch

# L = [x*x for x in range(10)]
# G = (x*x for x in range(10))
#
# print(L)
# for l in G:
#     print(l)


#斐波那契数列

# def feibo (max):
#     n , a ,b = 0,0,1
#     while n<max:
#         print(b)
#         a,b = b,a+b
#         n = n+1
#     return 'done'
#
# feibo(6)
#
# def feibo1 (max):
#     n , a ,b = 0,0,1
#     while n<max:
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return 'done'
#
# feibo1(6)

#这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行

# def odd():
#     print('第一步')
#     yield 1
#     print('第二步')
#     yield 2
#     print('第三步')
#     yield 3
#
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))


#杨辉三角
def triangles():
    l = [1]
    while True:
        yield l
        l = [0]+l+[0]
        l = [l[i]+l[i+1] for i in range(len(l)-1)]
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')