import random


#提出懷疑  fade out  暴怒/爆笑 日常慣例       ""以上這些沒有納入題目""
a_list = ["Mazu pilgrimages","without exoggeration","It is no exoggeration to say that","authorities concerned","cast a vote","cast a spell on","fade away","fade in","a throng of","put on a concert","plerce through","had his ears piered","emerge from","a blessing is disguise","offer sb's hospitality","be hospitable to","be enthusiastic about","sport facilities","seek cheap accommodations","for religion reasons","ancient ritual","designate the crisis a national emergency","designated driver","religious belief","culture heritage"]  
q_list = ["M__  __s媽祖繞境(2)","w__  __n不誇大(2)","I__ __ __ __ __ __ __t說...也不誇張(7)","a__  __d有關當局(2)","c__ __ __e投票(3)","c__ __ __ __n對...施咒(4)","f__  __y逐漸消失(2)","f__  __n淡入(2)","a __  __f一群(3)","p__ __ __ __t辦演唱會(4)","p__  __h穿過(2)","h__ __ __ __d穿耳洞(4)","e__  __m從...出現(2)","a __ __ __e塞翁失馬(4)","o__ sb's __y對某人盛情款待(4)","b__ __ __o對...好客(3)","b__ __ __t對...有熱情(3)","s__ __s運動設施(2)","s__ __ __s尋找便宜住宿(3)","f__ __ __s因為宗教因素(3)","a__ __l古老儀式(2)","d__ __ __ __ __ __y江浙狀態指定為國家緊急狀態(6)","d__ __r指定駕駛(2)","r__ __f宗教信仰(2)","c__ __e文化遺產"]
print("注意事項:如果不想繼續回答請輸入1")
keep = True


while keep == True:
    num = random.randint(0,13)
    answer = input(q_list[num])
    if a_list[num] == answer:
        print("正確")
    elif answer == "1" :
        print("結束")
        keep = False
    else:
        print("錯誤，正確答案為" + a_list[num])


