# if 语句案例
# 老师对大家的考试成绩进行评定，采用ABCDE五级进行评定，A是最好成绩
# 如果90分（包含此分数）以上，则输出A
# 如果80分（包含此分数）以上，则输出B
# 如果70分（包含此分数）以上，则输出C
# 如果60分（包含此分数）以上，则输出D
# 其余，则输出E
score = int(input("请输入您本次的考试成绩："))
if (score >= 90):
    print("A")
if (score >= 80 and score < 90):
    print("B")
if (score >= 70 and score < 80):
    print("C")
if (score >= 60 and score < 70):
    print("D")
if (score < 60):
    print("E")
#或者
print("或者：")
score = int(input("请输入您本次的考试成绩："))
if (score >= 90):
    print("A")
elif (score >= 80 ):
    print("B")
elif (score >= 70 ):
    print("C")
elif (score >= 60 ):
    print("D")
elif (score < 60):
    print("E")

#或者
print("或者：")
score = input("请输入您的成绩：")
score = int(score)
if (score >=90):
    print("A")
    print("Your are the best!")
    print("Thank you!")
else:
    if (score >= 60):
        print("成绩合格")
    else:
        print("对不起，重考！")