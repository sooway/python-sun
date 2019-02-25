#从今天00:00:00起，已经过去了28762秒，求现在是几时几分几秒
#分析：
#一个小时是3600s
#一分钟是60s
#如果知道总秒数，对小时的秒数求整就应该是小时，求余就是剩下的分秒对应的秒数，“//“
#对剩下的秒数用60求整，就会得到分钟数，剩下的就是秒数
s_sum = 28762
clock = s_sum // 3600
s_sum = s_sum % 3600
minu = s_sum //60
s_sum =s_sum % 60
print("现在是：%d时 %d分 %d秒" %(clock,minu,s_sum))
#或者
clock_sec = 3600
minu_sec = 60
s_sum = 28762
clock = s_sum // clock_sec
s_sum = s_sum % clock_sec
minu = s_sum // minu_sec
s_sum = s_sum % minu_sec
print("现在是：%d时 %d分 %d秒" %(clock, minu, s_sum))