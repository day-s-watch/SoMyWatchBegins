#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import PIL.Image as Image

'''
difference函数是本代码段中，最为基础的一个函数，其在对于两个list类型的参数对象进行处理
（我们可以合理推测，在python的代码处理中，最终图片类型都被转换为了list类型的序列）
在判断中，如果两个list相同位置值一致，那么就记录+1进行标注
如果不一致，则算出hist1与hist2的差值绝对值，除以hist1、2中的大值（可理解为差异的百分比）
用1相减，留存的也是相似度值，最后返回总体百分比
'''
def difference(hist1,hist2):
    sum1 = 0
    for i in range(len(hist1)):
       if (hist1[i] == hist2[i]):
          sum1 += 1
       else:
           sum1 += 1 - float(abs(hist1[i] - hist2[i])) / max(hist1[i], hist2[i])
    return sum1/len(hist1)


def similary_calculate(path1, path2, mode):
    if(mode == 3):
        img1 = Image.open(path1).resize((8,8)).convert('1')
        img2 = Image.open(path2).resize((8,8)).convert('1')
        hist1 = list(img1.getdata())
        hist2 = list(img2.getdata())
        return difference(hist1, hist2)

    # 预处理
    img1 = Image.open(path1).resize((256,256)).convert('RGB')
    img2 = Image.open(path2).resize((256,256)).convert('RGB')
    if(mode == 1):
        return difference(img1.histogram(), img2.histogram())
    if(mode == 2):
        sum = 0
        for i in range(4):
            for j in range(4):
                hist1 = img1.crop((i*64, j*64, i*64+63, j*64+63)).copy().histogram()
                hist2 = img2.crop((i*64, j*64, i*64+63, j*64+63)).copy().histogram()
                sum += difference(hist1, hist2)
                #print difference(hist1, hist2)
        return sum/16
    return 0


def readfolder(folder, pic, mode):
# 不同的mode对应不同的类型
    file_list = []
    t = 0
    file_temp = ''
    for root,directors,files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root,filename)
            if (filepath.endswith(".png") or filepath.endswith(".jpg")):
               remember = similary_calculate(folder+pic,folder+filename,mode)
               print filename
               print remember
               if (remember > t) and remember != 1:
                   file_temp = filename
                   t = remember

    return file_temp

