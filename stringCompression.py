#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 12:46:32 2019

@author: sinsakuokazaki
"""
#O(p + k^2):p is the size of the original string and k is number of character sequences.
def stringCompression(st):
    stLower = st.lower()
    count = 0
    newString = ""
    for i in range(len(stLower)):
        count += 1
        
        if i + 1 >= len(stLower) or stLower[i] != stLower[i + 1]:
            newString += stLower[i] + str(count)
            count = 0
    return newString if len(newString) < len(stLower) else st

#Sample answer1: string builder O(p+k)
def compress2(st):
    stringBuilder = []
    count = 0 
    for i in range(len(st)):
        count += 1
        if i + 1 >= len(st) or st[i] != st[i + 1]:
            count = str(count)
            stringBuilder.append(st[i])
            stringBuilder.append(count)
            count = 0
    compressed = "".join(stringBuilder)
    return compressed if len(compressed) < len(st) else st

#Sample ansewer2:
def compress3(st):
    finalLength = countCompression(st)
    
    stringBuilder = []
    count = 0 
    if finalLength >= len(st): return st
    stringBuilder = []
    count = 0 
    for i in range(len(st)):
        count += 1
        if i + 1 >= len(st) or st[i] != st[i + 1]:
            count = str(count)
            stringBuilder.append(st[i])
            stringBuilder.append(count)
            count = 0
    compressed = "".join(stringBuilder)
    return compressed
    
def countCompression(st):
    length = 0
    count = 0
    for i in range(len(st)):
        count += 1
        if i + 1 >= len(st) or st[i] != st[i + 1]:
            length += len(str(count))
            count = 0
    return length
