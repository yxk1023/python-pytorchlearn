import torch
x = torch.empty(2,3)
print(x)
print(x.size())

y = torch.rand(2,3)
print(y)
print(y.size())

# z = torch.zeros([5,3],dtype=torch.long)
# print(z)
# print(z.size())
#
# a = torch.tensor([5.33,2.23])
# print(a)
#
# y.add_(x)       #：PyTorch操作inplace版本都有后缀_, 例如x.copy_(y), x.t_() 就是原地操作的意思
# print(y)
#
# z = x[0,:]
# print(z)
# z += 1
# print(x[0,:])
# z = x.view([-1,2])
# print(z)
# print(z.size())
#
#
# t = torch.rand(1)
# print(t.item())
a = torch.arange(1,3).view(1,2)
b = torch.arange(1,4).view(3,1)
print(a)
print(b)
print(a+b)