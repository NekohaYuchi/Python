#L3.如何使用數字以及數字的用法2021/6/30

number = 8
print(number*5)
# 兩條//就可以只取整數
print(-77.1//5)
#python是有先乘除後加減的
print(8+8*5)
#python 是有先做括號的
print((8+8)*5)
#取餘數用%
print(number%5)


#函式介紹1 str
number = 8
print("會印出數字" + str(number))
#這樣印出來的就相當於是"8"也就是字串


#這樣是會Error的，因為字串跟數字是不能相加的
print(8 + str(number))


#函式介紹2 abs
number = -8
print(abs(number))
#abs就是取絕對值


#函式介紹3 pow
print(pow(2,4))
#這樣就是2的4次方
#所有數字的0次方就等於1


#函式介紹4 max
print(max(2,3,88,100,124,58,63))
#不管傳幾個數字進去都可以，他會給出裡面最大值


#函式介紹5 min
print(min(2,3,88,100,124,58,63))
#不管傳幾個數字進去都可以，他會給出裡面最小值


#函式介紹6 round
print(round(4.4))
#round的功能就是四捨五入


#引入其他數學函式
from math import *

#1.無條件捨去 floor
print(floor(4.4))

#2.無條件進位 ceil
print(ceil(4.4))

#3.開根號 sqrt
print(sqrt(64))