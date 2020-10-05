import torch
import numpy as np
from collections.abc import Iterable
from collections.abc import Iterator


print(isinstance('s',Iterable))
print([x for x in range(10)])
print(isinstance(111,Iterable))
print(isinstance((x for x in range(2)),Iterator))
print(isinstance([1,2],Iterator))
print(isinstance('abc',Iterator))

