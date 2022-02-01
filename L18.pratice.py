#L18.問答程式2021/7/8

from question import Question
#上面是在question.py只引入Question
import question
#上面是引入整個question.py
#做好question.py記得run一下，不然引入不了
test = [
    "1+3=?\n(a) 2\n(b) 3\n(c) 4\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
]


questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]
#括號後面的,要記得

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
        
    print("你得到" + str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)

#自己嘗試區
from question import Question
Text = [
    "Hololive裡面誰是菁英? \n(a) Miko\n(b) Pekora\(c) Rushia\n(d)Runa\n\n",
    "2021年的Minecraft夏日祭典是由哪個建設舉辦的? \n(a) 不知火建設\n(b) Akukin建設\n(c)兔田建設\n(d) 以上皆是 \n\n",
    "hololive裡面被稱為海豹的是\n(a) rami\n(b) nene\n(c) sora\n(d) roboko\n\n" 
]

questions = [
    Question(Text[0],"a"),
    Question(Text[1],"c"),
    Question(Text[2],"b")
]

def run_test(questions):
    scores = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            scores += 1
    
    print("你得到" + str(scores) + "分，共" + str(len(questions)) + "題")

run_test(questions)       