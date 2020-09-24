def myabs (x):
    if not isinstance(x,(int,float)):
        raise TypeError('错误的类型')
    if x<0:
        x = -x
        return x