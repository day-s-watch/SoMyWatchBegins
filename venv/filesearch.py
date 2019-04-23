import time
import os

#Read fime name
FileName = '/home/pi/Project/python/untitled/similarity/t2.jpg'
picFolder = '/home/pi/motion-images/'


def findlast(folder):
    fileTemp = ''
    lastTime = 0
    for root, directors, files in os.walk(folder):
        for filename in files:
            if (filename.lower()).endswith(".png") or (filename.lower()).endswith(".jpg"):
                #print filename
                # get modified time
                #print os.stat(folder+filename).st_mtime
                if lastTime < os.stat(folder+filename).st_mtime:
                    lastTime = os.stat(folder+filename).st_mtime
                    fileTemp = filename
    return fileTemp


#print file creation time
#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(FileName).st_ctime))
#print file modified time
#print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.stat(FileName).st_mtime))

print findlast(picFolder)
