#L14. 2維列表，巢狀迴圈2021/7/5
#row = 行
#column = 列

nums = [
    [0,1,2], 
    [3,4,5], 
    [6,7,8],
    [9]
]

print(nums[2][0])
#前面代表的是第幾行
#後面代表的是第幾列
#注意一樣是從0開始

for row in nums:
    for col in row:
        print(col)


#三維
nums = [
    [[0,1,2]], 
    [3,4,5], 
    [6,7,8],
    [9]
]

print(nums[0][0][1])
#增加一個維度就增加一個中括號就好了