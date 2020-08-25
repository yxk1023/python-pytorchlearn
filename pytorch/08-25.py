import torch
import numpy as np
# a = torch.arange(1,3).view(1,2)
# b = torch.arange(1,4).view(3,1)
# print(a)
# print(b)
# print(a+b)
# x= torch.tensor([1,2])
# y = torch.tensor([4,5])
# print(id(y))
# # torch.add(x,y,out=y)
# y.add_(x)
# print(id(y))
# b = x.numpy()
# print(b)

# c = torch.from_numpy(b)       from_numpy 得到的tensor与原来的numpy array共享内存，修改原来的数值 对应的tensor也会随之而改变
# print(c)
# b+=1
# print(b,c)

# c = torch.tensor(b)                 #直接用torch.tensor()将NumPy数组转换成Tensor，需要注意的是该方法总是会进行数据拷贝，返回的Tensor和原来的数据不再共享内存。
# print(c)                            #可以看到 b 加了1 ，c没有加1了
# b+=1
# print(b ,c)

# x = torch.ones((3,3,2))
# if torch.cuda.is_available():
#     device = torch.device("cuda")
#     y = torch.ones_like(x,device=device)
#     x = x.to("cuda")
#     z = x+y
#     print(z)
#     print(z.to("cpu"))

# x = torch.ones(2,2,requires_grad=True)
# print(x)
# print(x.grad_fn)
# y = x +2
# print("y:{} ;\n y.grad_fn :{}".format(y ,y.grad_fn))
#
# print(x.is_leaf ,y.is_leaf)         #x是叶子节点
# z= y*y*3
# out= z.mean()
# print(z,out)
# out.backward()
# print(x.grad)
#
# out2 = x.sum()
# out2.backward()
# print(x.grad)
#
# out3 = x.sum()
# x.grad.data.zero_()
# out3.backward()
# print(x.grad)

# a = torch.ones(2,2)
# a = a+1
# print(a.requires_grad)
# a.requires_grad_(True)
# print(a.requires_grad)
# b = (a *a).mean()
# print(a)
# print(b)
# print(b.grad_fn)
# b.backward()
# print(a.grad)

# x = torch.tensor([1,2,3,4],requires_grad=True,dtype=torch.float)
# y = 2*x
# z = y.view((2,2))
# print(z)
#
# v = torch.tensor([[1,0.1],[0.01,0.001]],dtype=float)
# z.backward(v)
# print(x.grad)

# x = torch.tensor(1,requires_grad=True,dtype=torch.float)
# y1 = x**2
# with torch.no_grad():
#     y2 = x**3
# y3 = y1 + y2
# print(y1, y1.requires_grad)
# print(y2, y2.requires_grad)
# print(y3, y3.requires_grad)
# y3.backward()
# print(x.grad)

x = torch.ones(1,requires_grad=True)
print(x.data)
print(x.data.requires_grad)
y = x**2
y.backward()
print(x)
print(x.grad)