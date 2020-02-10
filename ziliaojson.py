#!python3
import json
from glabdata import *
# {
#     "title": "小学数学同步[二年级上]",
#     "tips": "二年级上",
#     "course": "数学",fc hvgn cbv
#     "type": "jpg",
#     "sid": "math_qd_tongbu_2up",
#     "ver": "青岛版"
# }

# sid 命名规则 文件类型+文件名+年级+版本
# eg sid = mp3_english_book_1x_wys

#标题列表 

titleList = ['外研社一年级起小学英语音频']
titleList = {
    '外研社一年级起小学英语音频':'外研社一年级起小学英语音频'
}
# title = titleList[0]



def createZiliao(type,book,engver,ctitle,course,ver,year='all'):
    if(year == 'all' or year == 's' or year == 'x'):
        if(year == 'all'):
            years = yearList
            tipslist = tipList
        if(year == 's'):
            years = yearList[::2]
            tipslist = tipList[::2]
        if(year == 'x'):
            years =  yearList[1::2]
            tipslist = tipList[1::2]
        print(len(years))
        for i in range(len(years)):
            sidlist = [type,book,years[i],engver]
            sid = ('_'.join(sidlist))
            title = ctitle+'['+tipslist[i]+']'
            tips = tipslist[i]
            # course = courseList[0]
            # type = typeList[0]
            # ver = verList[0]
            strobj = '{{"title":"{}","tips":"{}","course":"{}","type":"{}","sid":"{}","ver":"{}"}}'.format(title,tips,course,type,sid,ver)
            f.write(strobj)
    else:
        years = year  
        newindex = yearList.index(year)
        print('newindex is'+str(newindex))
        sidlist = [type,book,year,engver]
        sid = ('_'.join(sidlist))
        title = ctitle+'['+tipList[newindex]+']'
        tips = tipList[newindex]
        print(tips)
        strobj = '{{"title":"{}","tips":"{}","course":"{}","type":"{}","sid":"{}","ver":"{}"}}'.format(title,tips,course,type,sid,ver)
        f.write(strobj)
    
    print(years)


f = open(r'D:/jielong/resources/ziliao.json','a',encoding="utf-8")
createZiliao(typeList['mp3'],booklist['english_book'],engverList['wys'],titleList['外研社一年级起小学英语音频'],courseList['english'],verList['wys'],'s')

# f.write(json.dumps(strobj,ensure_ascii=False))
f.close()
