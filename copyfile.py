# !python3
import shutil
import os

originfile = 'D:/jielong/pachong/english_mp3/1x.json'

for i in range(5):
    objectfile = 'D:/jielong/pachong/english_mp3/'+str(1+i+1)+'x.json'

    print(objectfile)

    shutil.copyfile(originfile,objectfile)