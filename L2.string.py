#L2.如何使用字串，字串的用法2021/6/28

# 函式Function
#這個函式功能是幫我們把字串裡面全部變成小寫
#.lower()是都變小寫.upper()是都變大寫
#.isupper()是幫我們看是否裡面的都是大寫，如果是就會傳True，反之會傳False
#.islower()是幫我們看是否裡面的都是小寫，如果是就會傳True，反之會傳False
phrase = "Hello Mr.White"
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.islower())


#函式的運算是可以做疊加的
print(phrase.lower().islower())


#有關[]的用法
print(phrase[0])
#這樣就會回傳字串的第一個字，也就是H給我
#重要! Python是從0開始算的


#這是找位置在第幾位的，如H在第0位
print(phrase.index("H"))
#如果要找的東西有很多個，如l，他會回傳最前面的位置，範例:
print(phrase.index("l"))
#這樣會出現的就會是2而不是3


#替換函式用法
print(phrase.replace("H","h"))
#這樣就會去字串內找到H並把他替換成h
#但是從我自己的觀察似乎並不會影響到全體的H


#\n就是換行的意思(注意這裡的\是Enter上面的\)
print("Hello \nMr.White")


#如果想要印出Hello "Mr.White
print("Hello \"Mr.White")


#也可以+起來
print("Hello" + " Mr.White")