#L9.建立進階計算機2021/7/3

#input是會輸出字串，所以我們可以用float轉換成數字
from typing import AsyncIterator


num1 = float(input("請輸入第一個數:"))
op = input("請輸入運算符號:")
num2 = float(input("請輸入第二個數:"))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2) 
elif op=="*":
    print(num1*num2) 
elif op=="/":
    print(num1/num2) 
else:
    print("不支援的運算")


