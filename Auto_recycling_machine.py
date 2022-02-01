#Side project Auto recycling machine 2021/7/8
bottles_number = 0
good_bottle = False
money = 0
start = False
over = False
length = input("偵測瓶子長度")
width = input("偵測瓶子寬度")
height = input("偵測瓶子高度")

def start(yes,no):
    if yes ==1 and no ==0:
        start =True
    elif yes ==0 and no ==1:
        start =False
    return start
#會做一個按鍵，一旦按下第一次開始鍵/停止鍵將會發出yes == 1,no ==0
#按下第二次開始鍵/停止鍵將會發出yes == 0,no ==1

def detect(length,width,height):
    if int(length) <= 30 and int(width) <= 10 and int(height) <=10:
        good_bottle = True
    else:
        print("很抱歉，這個瓶子不符合回收標準")
    return good_bottle

start(1,0)
detect(15,5,5)

while start == True:
    detect(length,width,height)
    bottles_number += 1
    if good_bottle ==True:
        print("成功累計")
        good_bottle = False
    else:
        bottles_number -= 1

money = bottles_number*0.5

#會做一個按鍵，一旦按下第一次結束鍵將會發出over == True
if over == True:
    print("非常感謝您的使用\n您一共回收了" + str(bottles_number) + "個瓶子\n一共可以折價" + str(money) + "元\n感謝您的使用\n歡迎您下次再來") 

over = False 



