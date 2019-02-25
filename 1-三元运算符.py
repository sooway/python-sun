#1、a,b两数由用户输入
#2、比较大小，把最大值存入变量c
# 分析：
#1、用户输入可以用input函数，然后用int转换
#2、比较两数，把大值存入c
a = input("请输入数字A:")
a = int(a)
b = int(input("请输入数字B："))
c = a if  a>b else b
print(c)

##作业：利用三元运算符求最大值
#-要求：
#1、a,b,c由用户输入三个
#2、比较大小，最大值输出

a = int(input("请输入A："))
b = int(input("请输入B："))
c = int(input("请输入C："))
d = (a if a>b else b) if (a if a>b else b)>c else c
print(d)