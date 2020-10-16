import torch
import numpy as np

# print(abs(-10))
# print(abs)
# f = abs
# print(f)    #结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# print(f(-10))   #变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。

#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def add (x,y,f):            #函数也是一个变量参数
    return f(x)+f(y)

print(add(-5,6,abs))        #当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs
