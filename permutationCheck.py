#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 14:25:35 2019

@author: sinsakuokazaki
"""

#my answer 
def permutation(st1, st2):
    #I forgot this sentence
    if len(st1) != len(st2):
        return False
    permutationHelper(st1, "")
    for perm in permList:
       if perm == st2:
           return True
    return False

permList = []
def permutationHelper(st, prefix):
    if len(st) == 0:
        permList.append(prefix)
        
    for i in range(len(st)):
        rem = st[:i] + st[i+1:]
        permutationHelper(rem, prefix + st[i])
     

#Sample ansewer1: Sort string
def permutationCheck(s, t):
    if len(s) != len(t):
        return False
    sSort = "".join(sorted(s))
    tSort = "".join(sorted(t))
    return sSort == tSort

#sample ansewer2: Check if the two string have identical character counts.
def permutationCheck2(s, t):
    if len(s) != len(t):
        return False
    sList = list(s)
    charNum = {}
    for k in sList:
        charNum[k] = sList.count(k)
    for x in t:
        if x in charNum.keys():
            if charNum[x] > 0:
                charNum[x] -= 1
        else: return False
    return True
            