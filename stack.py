#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:27:23 2019

@author: sinsakuokazaki
"""

class Stack:
    def __init__(self, stacklen):
        self.stacklen = stacklen
        self.array = [0] * stacklen
        self.size = 0
        self.minnum = None
        
    def push(self, item):
        if self.isFull:
            raise('Stack is full')
        self.size += 1
        self.array[self.size] = item
        if minnum and minnum > item:
            self.minnum = item
    
    def pop(self):
        if self.isEmpty:
            raise('Stack is empty')
        value = self.array[self.size]
        self.array[self.size] = 0
        self.size -= 1
        return value
    
    def __min__(self):
        
        
    
    def isFull(self):
        return self.size == self.stacklen
            
    def isEmpty(self):
        return self.size == 0
    
