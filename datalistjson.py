#!python3
import json

# {
#     "type": "pdf",
#     "uripath": "cloud://dev1-vo13f.6465-dev1-vo13f-1300553401/pdf/book/二年级上_青岛版.pdf",
#     "tips": "二年级上",
#     "title": "二年级上_青岛版.pdf",
#     "sid": "math_qd_book_2up",
#     "ordernum": 0
# }
respath = 'sfd'
envpath = ['cloud://dev1-vo13f.6465-dev1-vo13f-1300553401/','cloud://pre-71s05.7072-pre-71s05-1300553401/']
uripath = str(envpath[0])+respath
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
 
sid="asdf"
typeList = ['mp3','pdf','jpg','word','excel','html']
title = ''
ordernum = 0

f = open(r'D:/jielong/resources/datalist.json','a',encoding="utf-8")
strobj = '{{"title":"{}","tips":"{}","ordernum":{},"type":"{}","sid":"{}","uripath":"{}"}}'.format(title,tipList[1],ordernum,typeList[0],sid,uripath)
# print(strobj)
f.write(strobj)
# f.write(json.dumps(strobj,ensure_ascii=False))
f.close()