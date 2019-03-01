#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:42:40 2019

@author: sinsakuokazaki
"""
"""
def polindrome(st):
    permutation(st, "")
    for pre in prefixList:
        preL = list(pre)
        preFirst = preL[:len(preL) / 2]
        preLast = preL[(len(preL) / 2) - 1:]
        preLast.reverse()
        result = []
        for i in range(len(preL) / 2):
            if preFirst[i] != preLast[i]:
                pass
            else: 
                continue
        result.append(prefixList)
       
        
        
        if len(preL) % 2 == 0:
            
            for i in range(len(pre)/2):
                if
           
        else:
            for i in range(len(st) + 1 / 2):
            
preixList = []
def permutation(st, prefix):
    if len(st) == 0:
        preList.append(prefix)
    for i in range(len(st)):
        rem = st[:i] + st[i+1:]
        permutation(rem, prefix + st[i])
"""
#Sample: To permutation of a palindrome, string can have no more than one character that is odd.
def isPermutationOfPalindrome(phrase):
    table = buildCharFrequencyTable(phrase)
    return checkMaxOneOdd(table)
#Check that no more than one character has an odd count
def checkMaxOneOdd(table):
    foundOdd = False
    for k in table.keys():
        if table[k] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    return True
#Map each character to a numeber. a -> 0. b -> 1, c -> 2
#This is case insensitive. Non-letter characters map to -1
def getCharNumber(c):
    if ord(c) >= ord("a") and ord(c) <= ord("z"):
        return ord(c)
    return -1
#Count how many times each character appears.
def buildCharFrequencyTable(phrase):
    table = {}
    for c in phrase:
        num = getCharNumber(c)
        if num != -1:
            if c not in table.keys():
                table[c] = 1
            else: table[c] += 1
    return table 
    
    