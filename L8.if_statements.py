#L8.if判斷句2021/7/3

#1.
#如果 我肚子餓
#    我就去吃飯
hungry = True
if hungry:
    print("我就去吃飯")
#如果上面的hungry = False那就會略過去執行下面的程式碼


#2.
#如果 今天下雨
#    我就開車去上班
#否則
#    我就走路去上班
rainy = True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班") 
#rainy = True，執行if。rainy = False，執行else


#3.
#如果 你考100分
#    我給你1000元
#或是如果 你考80分以上
#    我給你500元
#或是如果 你考60分以上
#    我給你100元
# 否則
#    你給我300元
scores = 100
if scores==100:
    print("我給你1000元")
elif scores>=80:
    print("我給你500元")
elif scores>=60:
     print("我給你100元")
else:
    print("你給我300元")
#=是把右邊的值放到左邊裡面
#==是比較左邊的值跟右邊的值有沒有相等


#4.
#如果 你考100分 且 今天下雨
#    我給你1000元
#否則
#    你就給我100元
score = 100
rainy = True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")
#and左邊跟右邊都要符合才會把一整段變成True


#5.
#如果 你考100分 或 今天下雨
#    我給你1000元
#否則
#    你就給我100元
score = 100
rainy = True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")
#or左邊或右邊其中一個符合就會把一整段變成True


#6.
#如果 你考100分 或 沒有下雨
#    我給你1000元
#否則
#    你就給我100元
score = 100
rainy = True
if score!=100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")
#score!=100這句話是在問說score是不是不等於100


#練習
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else: 
        return num3

print(max_num(2,5,3))