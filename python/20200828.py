# age = int(input("请输入你的年龄\n"))
# if age >=18:
#     print("你已经成年了，是个大人了")
# elif age>=13:
#     print("你还未成年，但是你是青少年了，犯法要接受法律的制裁")
# else:print("你还小，但是不要当熊孩子，要不然以后政府教育你")
# b = str(age)
# print(b)


# height=float(input("请输入您的身高\n"))
# weight=float(input("请输入您的体重\n"))
# bmi = weight/(height**2)
# if bmi>32:
#   print("严重肥胖")
# elif 32>=bmi>28:
#   print("肥胖")
# elif 28>=bmi>25:
#   print("过重")
# elif 25>=bmi>18.5:
#   print("正常")
# else:print("过轻")
# print("您的BMI指数为：{}".format(bmi))

# a = [1,2,3,4,5,6]
# for o in a:
#     print(o)

# sum = 0
# for i in range(5,7):
#     sum=sum+i
#     print(i)
# print(sum)

# i = 1
# sum = 0
# while i<100:
#     sum = sum +i
#     i+=2
# print(sum)

# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#   print("Hello,%s"%i)
#   print("Hello,{}{}".format(i,i))

n = 1
while n<100:
    n=n+1
    if n%2==0:
        continue
    print(n)
print('end')