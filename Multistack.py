#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:07:17 2019

@author: sinsakuokazaki
"""

class MultiStack:
    
    def __init__(self, stacksize):
        self.numstacks = 3
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * (stacksize)
        self.stacksize = stacksize
        
    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item
        
    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value
    
    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]
            
    def IsFull(self, stacknum):
        return self.stacksize == self.sizes[stacknum]
    
    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0
    
    def IndexOfTop(self, stacknum):
        offset = self.stacksize * stacknum
        return offset + self.sizes[stacknum] - 1
    

def ThreeInOne():
    newstack = MultiStack(2)
    print(newstack.IsEmpty(1))#True
    newstack.Push(3, 1)
    print(newstack.Peek(1))#3
    print(newstack.IsEmpty(1))#False
    newstack.Push(2, 1)
    print(newstack.Peek(1))#2
    print(newstack.Pop(1))#2
    print(newstack.Peek(1))#3
    newstack.Push(3, 1)

ThreeInOne()
