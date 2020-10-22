import numpy as np
import torch
def is_odd(n):
    return n%2==1
a = filter(is_odd,[1,2,3,4,5,6,7])  #可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
                                    #注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
                                    # 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
print(list(a))
