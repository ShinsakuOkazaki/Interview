#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:10:50 2019

@author: sinsakuokazaki
"""
#My answer
def spaceReplace(stIn):
    lIn = list(stIn)
    for i in range(len(lIn)):
        if lIn[i] == " ":
            lIn[i] = "%20"
    for i in range(len(lIn)):
        if lIn[-1] ==  "%20" and lIn[-2] == "%20":
            lIn.pop()
        break
    lIn.pop()
    lIn.pop()
    return "".join(lIn)


ip = "Mr John Smith    "

#Sample answer: start edinting from end, because we know that it has extra spaces.
def spaceReplace2(st, trueLength):
    stList = list(st)
    spaceCount = 0
    for i in range(trueLength):
        if stList[i] == " ":
            spaceCount += 1
    index = trueLength + spaceCount * 2
    for i in range(trueLength-1, -1, -1):
        if stList[i] == " ":
            stList[index - 1] = "0"
            stList[index - 2] = "2"
            stList[index - 3] = "%"
            index = index - 3
        else:
            stList[index - 1] = stList[i]
            index -= 1
    return "".join(stList)
            