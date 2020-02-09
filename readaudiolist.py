# !python 3
import json
import os
import requests

f = open(r'D:/jielong/pachong/english_mp3/6x.json','r',encoding="utf-8")
pathurl = r'D:\jielong\data\mp3\englishbook\6x'

if(os.path.isdir(pathurl)):
    pass
else:
    os.makedirs(pathurl)
          

jsonstr = f.read()

jsoncon = json.loads(jsonstr)
f.close()
for jsonitem in jsoncon:
    print(jsonitem['title'])
    print(jsonitem['src'])

    audiores = requests.get(jsonitem['src'])
    audiores.raise_for_status()
   

    audiofile = open(os.path.join(
        pathurl, os.path.basename(jsonitem['src'])), 'wb')
    for chunk in audiores.iter_content(500000):
        audiofile.write(chunk)
    audiofile.close()


# print(jsoncon)


# tre = json.loads(get_js())

# print(tre)