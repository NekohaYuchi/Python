#L4.建立一個基本計算機2021/7/1

#會讀取用戶的兩個輸入，再把這兩個數字相加印給我們
name = input("請輸入你的名字:")
age = input("請輸入你的年紀:")
print("哈囉" + name + "你今年" + age + "歲")


number1 = input("請輸入第一個數字:")
number2 = input("請輸入第二個數字:")
print(number1 + number2)
#input會預設把我們輸入的數字當成字串
#也就是說8+5會變成85
#有兩個函式可以解決當成字串的辦法

number1 = input("請輸入第一個數字:")
number2 = input("請輸入第二個數字:")
print(int(number1) + int(number2))
#int會把字串轉換成整數
#但是如果用小數相加int 就會出錯

#float會把字串轉換成小數
number1 = input("請輸入第一個數字:")
number2 = input("請輸入第二個數字:")
print(float(number1) + float(number2))
