#L13.for迴圈2021/7/4

#for 變數 in 字串或列表:
#    要重複執行的程式碼

for letter in "Hello Yuchi":
    print(letter)

for num in [0,1,2,3,4]:
    print(num)

for num in range(100):
    print(num)

for num in range(2,7):
    print(num)

#練習
#試著做出以下這個函式
print(pow(2,5))

#自己做的
num = 2  
while num != 32:
    if num == 32:
        print("32")
    else:
        num*2

#正解
def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result * base_num
    return result

print(power(2,6))

#自己聽後又做了一遍
def power(base_num,times):
    result = base_num 
    for Yuchi in range(times-1):
        result = result * base_num
    return result

print(power(2,5))