#L17.類別class,物件object2021/7/7

class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)
print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)

phone2 = Phone("andriod",456,False)
print(phone2.os)
print(phone2.number)
print(phone2.is_waterproof)

#以下為自己亂做的 
if phone1.os == "ios":
    print("ios") 
else:
    print("others")