import math
# def abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('输入的不是数字')
#     if x>=0:
#         return x
#     else:
#         return -x
# print(abs(-1))
# # age = 10
# # if age>18:
# #     pass
# def move (x,y,step=0,angle=0):
#     nx = x +step * math.sin(angle)
#     ny = y +step * math.sin(angle)
#     return nx ,ny
# x= move(1,2,3,math.pi/6)
# print(x)

def quadratic(a, b, c):
  x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
  x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
  return x1,x2
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')