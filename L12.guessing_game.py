#L12. 猜數字遊戲2021/7/4

#課程內容
secret_num = 77
guess = None

while secret_num != guess:
    guess = int(input("請輸入你猜的數字: "))
    if guess > secret_num:
        print("再小一點")
    elif  guess < secret_num:
        print("再大一點")
    
print("恭喜你猜到啦!")


#只能猜測5次
secret_num = 77
guess = None
guess_count = 0
guess_limit = 5
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("請輸入你猜的數字: "))
        if guess > secret_num:
            print("再小一點")
        elif  guess < secret_num:
            print("再大一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("很抱歉你輸了")
else:
     print("恭喜你猜到啦!")

    

#未上課之前先依靠自己手做
guess = input("請輸入你猜的數字:")
if guess == 68:
    print("恭喜你猜到啦!")
elif guess<68:
    print("再大一點")
elif guess>68:
    print("再小一點")