import torch
import numpy as np
from collections.abc import Iterable
from collections.abc import Iterator
import sys
#
# print(isinstance('s',Iterable))
# print([x for x in range(10)])
# print(isinstance(111,Iterable))
# print(isinstance((x for x in range(2)),Iterator))
# print(isinstance([1,2],Iterator))
# print(isinstance('abc',Iterator))
#
# print(isinstance(iter('abc'),Iterator))

#迭代器的创建
# list =[1,2,3,4]
# it = iter(list)
# print(next(it))
# print(next(it))

# a = [1,2,3,4]
# it = iter(a)              # 创建迭代器对象
# for x in it:
#     print(x,end="")


a = [1,2,3,4]       #使用 next() 函数实现：
it = iter(a)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
