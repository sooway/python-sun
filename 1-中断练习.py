##break语句
#break： 无条件结束整个循环，简称循环猝死
#continue：无条件结束本次循环，从新进入下一轮循环
#pass：表示略过，通常用于站位
for idx in range(50,100):
    print(idx)
    if idx % 9 ==0:
        print(idx)
        break

##第二个：
print("找到7并打印出来：")
for i in range(1,11):
    if i == 7:
        print("我找到了")
        break
    else:
        print(i)

print("在数字1-10中，寻找所有偶数，找到偶数后打印偶数")
for i in range(1,11):
    if i % 2 == 1:
        continue
    else:
        print("{0} 是偶数".format(i))

# pass例子，一般用于占位
# pass没有跳过功能
print("pass例子")
for i in range(1,11):
    pass
    print("wo zai zheli")