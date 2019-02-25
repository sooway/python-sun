#使用%进行格式化
#使用format函数，近年来比较流行
#%s表示简单的字符串
# s = "My name is %s" % "wangdapeng" 当只有一个需要替换的时候，可以省略括号
# %d表示一个数字（整数），如果后面实际是小数，则进行取整，舍弃后面小数
# %f表示浮点小数，可以在f前加 ".x"，x表示小数位数
# s = "I am %.2f" % 86.34
s = "My name is %s,my age is %d,i am %.2f, %dkg" % ('lidameng',38,173,80)
print(s)
d = "My name is {0},my age is {1}。".format("lidameng",18)
print(d)