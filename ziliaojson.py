#!python3
import json
# {
#     "title": "小学数学同步[二年级上]",
#     "tips": "二年级上",
#     "course": "数学",
#     "type": "jpg",
#     "sid": "math_qd_tongbu_2up",
#     "ver": "青岛版"
# }
title = "暗室逢灯"
tipList = [
        "一年级上",
        "一年级下",
        "二年级上",
        "二年级下",
        "三年级上",
        "三年级下",
        "四年级上",
        "四年级下",
        "五年级上",
        "五年级下",
        "六年级上",
        "六年级下"]
courseList = [
        "英语",
        "数学",
        "语文",
        "寒暑假"
    ]  
sid="asdf"
typeList = ['mp3','pdf','jpg','word','excel','html']
verList = ['人教版','青岛版','外研社']

f = open(r'D:/jielong/resources/ziliao.json','a',encoding="utf-8")
strobj = '{{"title":"{}","tips":"{}","course":"{}","type":"{}","sid":"{}","ver":"{}"}}'.format(title,tipList[1],courseList[0],typeList[0],sid,verList[0])
# print(strobj)
f.write(strobj)
# f.write(json.dumps(strobj,ensure_ascii=False))
f.close()
