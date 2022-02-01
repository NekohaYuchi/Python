#L15.檔案的讀取，寫入2021/7/5

#open("檔案路徑", mode = "開啟模式")
#絕對路徑 ex: C:/Users/hibyby/Desktop/python/123.txt
#相對路徑 以程式的位置做延伸 ex:  123.txt

#mode="r" 讀取
#mode="w" 覆寫
#mode="a" 在原先的資料後寫東西

file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "r")
#複製過來會長這樣:C:\Users\user\Desktop\Python  code
#我們需要把\改成/
print(file.read())
#做完要記得把檔案關起來
file.close()


file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "r")
print(file.readline())
print(file.readline())
file.close()


file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "r")
for line in file:
    print(line)
file.close()


file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "r")
print(file.readlines())
file.close()


# 覆寫
file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "w")
file.write("Hi")
file.close()


#在原先的資料後寫東西
file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "a")
file.write("Yuchi")
file.close()


#編碼方式並不支援中文
file = open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "a", encoding="utf-8")
file.write("\n Yuchi")
file.close()
#因此要加 encoding="utf-8"


#自動關閉的方法
with open("C:/Users/user/Desktop/Python  code/測試文件.txt", mode = "a", encoding="utf-8") as file:
    file.write("\n Yuchi")
#因為只要離開with就會自動close