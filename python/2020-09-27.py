import numpy as np
import torch
import math
import matplotlib.pyplot

l = [x*x for x in range(1,10,2)]
print(l)
x = [x*x for x in range(1,11) if x%2 ==0]
print(x)
n = [p+q for p in 'ABC' for q in str(123)]
print(n)
