#L5.列表List，列表的用法2021/7/1
scores = [90,70,60,50,80]
#這樣就不用像下面一樣要用五個變數
score1 = 90
score2 = 70
score3 = 60
score4 = 50
score5 = 80

print(scores)

friends = ["pekora","rushia","marin"]
print(friends)

things = [90,"pekora",True]
print(things)

#若要取得90的成績
print(scores[0])

#若要取得列表倒數第一位
print(scores[-1])

#若要取得90跟70的成績
print(scores[0:2])
#就是從0開始取到第2位，卻不包含第2位

#若要取得從70開始一路到結束的成績
print(scores[1:])

#若要取得80以前的成績
print(scores[:4])


#延伸應用
phrase = "Hello Mr.White"
print(phrase[0:5])


#假設我們的列表90,70,60,50,80，其中的第一個90打錯了，其實是30分
scores = [90,70,60,50,80]
scores[0] = 30
print(scores)


# 介紹函式1.extend
scores.extend(friends)
print(scores)
#把friends接到scores後面


# 介紹函式2.append
scores.append(60)
print(scores)
#會在scores後面再加上一個值


# 介紹函式3.insert
scores.insert(2,30)
print(scores)
#插入一個值進去，2代表第2位，30代表插入30


# 介紹函式4.remove
scores.remove(30)
print(scores)


# 介紹函式5.clear
scores.clear()
print(scores)
#清除列表


# 介紹函式6.pop
scores.pop()
print(scores)
#移除列表最後一位


# 介紹函式7.sort
scores.sort()
print(scores)
#會幫我們的列表由小到大做排列


# 介紹函式8.reverse
scores.reverse()
print(scores)
#會將我們的列表反轉


# 介紹函式9.index
print(scores.index(70))
# 會幫我們找到70在列表裡面的位置
#有兩個一樣的數字會回傳最前面的位置


# 介紹函式10.count
print(scores.count(70))
#他會回傳給我們列表裡面有幾個你要找的數字