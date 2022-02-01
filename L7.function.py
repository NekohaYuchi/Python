#L7.函式 function2021/7/2

def hello(name,age):
    print("hello" + name + "你今年" + age + "歲")
hello(" Yuchi","16")
#注意!這裡的16是字串，因為數字不能跟字串相加

def add(num1,num2):
    print(num1+num2)
  
add(2,3)


def add2(num3,num4):
      return num3+num4

print(add2(2,3))
#為什麼需要retune呢?
#是因為我們往往做完運算之後還要接著運算
#所以需要他回傳回來


#題目1:
#以下這串會印出什麼東西
def add(num1,num2):
    print(num1+num2)
    return 10

value=add(3,4)
print(value)
#答:7跟10 (自己答對了)
#詳解
#code是由上往下執行的，從def add(num1,num2):一路往下走
#在看到value=add(3,4)之後因為偵測到add回到上面相加print，所以先得7
#然後再return 10
#所以最後value=10，因為return把他覆蓋掉了
#最後再印出來print(value)
#這個是非常重要的


#題目2:
#以下這串會印出什麼東西
def add(num1,num2):
    print(num1+num2)

value=add(3,4)
print(value)
#答:7跟None (自己答錯了)
#詳解
#在定義函式的時候是一定要加return的
#如果不加的話Python會預設幫你reture None


#函式在運行的時候一碰到return就會直接結束
#不會再做下面的函式
#例
def add(num1,num2):
    print(num1+num2)
    return 10
    print("Hello")

value=add(3,4)
print(value)
#print("Hello")是不會被執行的喔