import torch
x = torch.empty(5,5)
print(x)
print(x.size())

y = torch.rand(5,5)
print(y)
print(y.size())

z = torch.zeros([5,3],dtype=torch.long)
print(z)
print(z.size())

a = torch.tensor([5.33,2.23])
print(a)

y.add_(x)       #：PyTorch操作inplace版本都有后缀_, 例如x.copy_(y), x.t_() 就是原地操作的意思
print(y)