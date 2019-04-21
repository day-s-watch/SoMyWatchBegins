#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import similarity as sim
import newcopy


#file global
difThreshold = 0.6
picFolder = '/home/pi/motion-images/'
alarmFlag = 0

if __name__ == '__main__':
    #print "相似度最高的图是" + sim.readfolder('/home/pi/Project/python/untitled/similarity/', 't2.jpg',1)
    lastPic = ''
    currentPic = ''
    tmp = 0

    #initialization
    lastPic = newcopy.findlast(picFolder)
    print lastPic

    #mainProgress
    while True:
        time.sleep(2)
        currentPic = newcopy.findlast(picFolder)
        print currentPic
        tmp = sim.similary_calculate(picFolder+lastPic, picFolder+currentPic, 1)
        if tmp <= difThreshold:
            alarmFlag = 1
            print tmp
            print alarmFlag
        else:
            alarmFlag = 0
            print alarmFlag
        lastPic = currentPic

    #clear up
