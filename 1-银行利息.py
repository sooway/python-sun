#已知有10000本金
#每年利息收入7%
#多少年后本金会超过13000
#分析：
#    循环问题
#    没有明确循环次数
#    循环条件确定：本金不超过13000
# 让我们求年限，我们用一个变量来存储答案并初始化
year = 0
money = 10000
while (money <= 13000):
    money = money * 1.07
    year = year + 1
print("Yeare is %d 年" % year)