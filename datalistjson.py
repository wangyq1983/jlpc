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
    "pdf_math_book":"pdf/mathbook/",
    "pdf_english_book":"pdf/englishbook/"
}
envpath = {
    "dev":"cloud://dev1-vo13f.6465-dev1-vo13f-1300553401/",
    "pre":"cloud://pre-71s05.7072-pre-71s05-1300553401/"
}

# 英语课本MP3
# uripath = str(envpath['dev'])+respath['mp3_english_book']+'6x/'

# 英语同步MP3
# uripath = str(envpath['dev'])+respath['mp3_english_tongbu']+'6s/'

# 青岛地区 教材 语数英pdf
uripath = str(envpath['dev'])+respath['pdf_english_book']

# mp3英语生成
# sidlist = [typeList['pdf'],booklist['chinese_book'],'6s',engverList['wys']]

# pdf生成
sidlist = [typeList['pdf'],booklist['english_book'],engverList['wys']]
sid=('_'.join(sidlist))

# title = ''
# ordernum = 0

# 生成json 适用于目录下多年级多文件 如英语MP3
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

# 生成json 适用于多年级单独文件 如数学pdf
def createData(ctype,curipath,mulu):
    list = os.listdir(mulu)
    for i in range(0,len(list)):
        title = os.path.join(list[i])
        tips = tipList[i]
        ordernum = 0
        type = ctype
        sidlist = [typeList['pdf'],booklist['english_book'],yearList[i],engverList['wys']]
        sid=('_'.join(sidlist))
        resuripath = curipath + os.path.join(list[i])
        strobj = '{{"title":"{}","tips":"{}","ordernum":{},"type":"{}","sid":"{}","uripath":"{}"}}'.format(title,tips,ordernum,type,sid,resuripath)
        print(strobj)
        f.write(strobj)

# MP3英语json
# jsonpath = r'D:/jielong/resources/mp3/englishtongbu.json'

jsonpath = r'D:/jielong/resources/pdf/englishbook.json'

f = open(jsonpath,'a',encoding="utf-8")
# 执行创建数据列表函数
# createDatalist(typeList['mp3'],uripath,'六年级上',sid,r"D:\jielong\data\mp3\englishtongbu\6s")

createData(typeList['pdf'],uripath,r"D:\jielong\data\pdf\englishbook")
# createDatalist()
# f.write(json.dumps(strobj,ensure_ascii=False))
f.close()