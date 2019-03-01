#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 19:44:27 2019

@author: sinsakuokazaki
"""

def  checkEdited(st, stEdited):
    #insert
    if len(stEdited) - len(st) == 1:
        #for c in st:
        #    if not c in stEdited: return False
        #return True
        index1 = 0
        index2 = 0
        while index2 < len(st) and index1 > len(stEdited):
            if st[index1] != stEdited[index2]:
                if index1 != index2:
                    return False
                index2 += 1
            else:
                index1 += 1
                index2 += 1
        return True
    #remove
    elif len(stEdited) - len(st) == -1:
        #for c in stEdited:
        #    if not c in st: return False
        #return True
        index1 = 0
        index2 = 0
        while index1 < len(st) and index2 > len(stEdited):
            if st[index1] != stEdited[index2]:
                if index1 != index2:
                    return False
                index1 += 1
            else:
                index1 += 1
                index2 += 1
        return True
    
    #replace
    elif len(stEdited) == len(st):
        #result = 0
        result = False
        for i, j in zip(st, stEdited):
            if i != j:
                #result += 1
                #if result > 1:
                if result:
                    return False
                result = True
        return True
    else: return False
        
#Sample Answer

def main():
    return checkEdited("pales","pale")

