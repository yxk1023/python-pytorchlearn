#
# print(chr(95))
# print('我')
list = ['wds',12,'A']
print(list)
print(len(list))
list.append('B')
list.insert(1,'插入的位置')
print(list)
list.pop()      #删除表尾的字符串
print(list)
list.pop(1)     #删除指定位置的元素
print(list)
list[0] = '替换的元素'
print(list)
list[0] = ['替换的','元素为数组']
print(list)
print(list[0])
print(list[0][0])
l=[]
print(len(l))