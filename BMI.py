height = float(input("請輸入您的身高cm:"))
weight = float(input("請輸入您的體重kg:"))
height = height*0.01
bmi = weight/(height*height)
print("您的BMI為" + str(bmi))
print("體重過輕:BMI ＜ 18.5\n正常範圍:18.5≦BMI＜24\n異常範圍:過重：24≦BMI＜27\n輕度肥胖：27≦BMI＜30\n中度肥胖：30≦BMI＜35\n重度肥胖：BMI≧35")



def bmi_count(height,weight):
    height1 = height*0.01
    bmi = weight/(height1*height1)
    print("您的BMI為" + str(bmi))
    print("體重過輕:BMI ＜ 18.5\n正常範圍:18.5≦BMI＜24\n異常範圍:過重：24≦BMI＜27\n輕度肥胖：27≦BMI＜30\n中度肥胖：30≦BMI＜35\n重度肥胖：BMI≧35")
    return bmi_count

print(bmi_count(175,56))

