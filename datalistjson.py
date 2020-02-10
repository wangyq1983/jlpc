#!python3
import json
from glabdata import *
import os
# {
#     "type": "pdf",
#     "uripath": "cloud://dev1-vo13f.6465-dev1-vo13f-1300553401/pdf/book/二年级上_青岛版.pdf",
#     "tips": "二年级上",
#     "title": "二年级上_青岛版.pdf",
#     "sid": "math_qd_book_2up",
#     "ordernum": 0
# }
respath = {
    "mp3_english_book":"mp3/englishbook/",
    "mp3_english_tongbu":"mp3/englishtongbu/",
    "pdf_chinese_book":"pdf/chinesebook/",
    "pdf_math":"pdf/mathbook/",
    "pdf_english":"pdf/englishbook/"
}
envpath = {
    "dev":"cloud://dev1-vo13f.6465-dev1-vo13f-1300553401/",
    "pre":"cloud://pre-71s05.7072-pre-71s05-1300553401/"
}
uripath = str(envpath['dev'])+respath['mp3_english_book']+'1x/'

sidlist = [typeList['mp3'],booklist['english_book'],yearList[0],engverList['wys']]
sid=('_'.join(sidlist))

# title = ''
# ordernum = 0

# 生成json
def createDatalist(ctype,curipath,ctips,csid,mulu):
     list = os.listdir(mulu)
     for i in range(0,len(list)):
        title = os.path.join(list[i])
        tips = ctips
        ordernum = i
        type = ctype
        sid = csid
        resuripath = curipath + os.path.join(list[i])
        strobj = '{{"title":"{}","tips":"{}","ordernum":{},"type":"{}","sid":"{}","uripath":"{}"}}'.format(title,tips,ordernum,type,sid,resuripath)
        print(strobj)
        f.write(strobj)
   
f = open(r'D:/jielong/resources/datalist.json','a',encoding="utf-8")
createDatalist(typeList['mp3'],uripath,tipList[1],sid,r"D:\jielong\data\mp3\englishbook\1x")
# createDatalist()
# f.write(json.dumps(strobj,ensure_ascii=False))
f.close()