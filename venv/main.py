#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import similarity as sim
import filesearch
import ConfigParser

#ConfigFileParserPart
conf = ConfigParser.ConfigParser()
conf.read("main.cfg")


#file global
difThreshold = conf.getfloat("main", "difThreshold")
picFolder = conf.get("main", "picFolder")
alarmFlag = conf.getint("main", "alarmFlag")
calcmode = conf.getint("main", "calcmode")

if __name__ == '__main__':
    #print "相似度最高的图是" + sim.readfolder('/home/pi/Project/python/untitled/similarity/', 't2.jpg',1)
    lastPic = ''
    currentPic = ''
    tmp = 0

    #initialization
    lastPic = filesearch.findlast(picFolder)
    print lastPic

    #mainProgress
    while True:
        time.sleep(2)
        currentPic = filesearch.findlast(picFolder)
        print currentPic
        tmp = sim.similary_calculate(picFolder+lastPic, picFolder+currentPic, calcmode)
        if tmp <= difThreshold:
            alarmFlag = 1
            print tmp
            print alarmFlag
        else:
            alarmFlag = 0
            print alarmFlag
        lastPic = currentPic

    #clear up
