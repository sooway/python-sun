#乘法表是一个典型双重for循环结构
#如果乘积大于36，结束本轮循环
#结束用break
#不能使用print语句，因为print语句默认输出后会换行
#在sys模块中有write可以使用
import sys
# 负责乘法表的行数
for i in range(1,10):
    # 负责乘法表的列数
    for j in range(1,10):
        if i*j > 81:
            break
        sys.stdout.write(str(i*j))
        sys.stdout.write(" ")
    print(" ")

#或者：
import sys
for i in range(1,10):
    for j in range(1,10):
        if i*j > 81:
            continue
        n = i*j
        n = str(n)
        sys.stdout.write( n )
        sys.stdout.write("  ")
    print("  ")
#或者
print("这种最好")
for i in range(1,10):
    for j in range(1,i+1):
        print( i * j,end=(" "))
    print("")