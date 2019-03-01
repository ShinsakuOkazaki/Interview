#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:10:19 2019

@author: sinsakuokazaki
"""


#check s2 is rotation of s1
#s1 = xy = waterbottle
#x = wat
#y = erbottle
#s2 = yx = erbottlewat
#yx is always subset of xyxy
#therefore, s2 is always subset of s1s1

def isCheckRotation(s1, s2):
    length = len(s1)
    if length == len(s2) and length > 0:
        s1s1 = s1 * 2
        return s2 in s1s1
    return False