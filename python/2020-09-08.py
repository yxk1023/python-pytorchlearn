def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s=s*x
    return s
print(power(5))
def enroll (name ,gender,age=5,city='shanghai'):
    print('name:{}'.format(name))
    print('gender:{}'.format(gender))
    print('age:{}'.format(age))
    print('city:%s',city)
enroll('nima','女',city='beijing',age=66)

# def add_end (l=[]):
#     l.append('end')
#     return l
# print(add_end([1,'ss',3]))
# print(add_end())
# print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())