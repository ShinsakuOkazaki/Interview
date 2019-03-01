#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:11:29 2019

@author: sinsakuokazaki
"""

class LinkedListNode():
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode
    def __str__(self):
        return str(self.value)
    
class LinkedList():
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_multiple(values)
            
    def __iter__(self):
        current = self.head
        while current:
            yield current 
            current = current.next
            
    def __str__(self):
        values = [str(x) for x in self]
        return '->'.join(values)
    
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return current
    
    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple(self, values):
        for v in values:
            self.add(v)
    

ll = LinkedList()
ll.add_multiple([0, 1, 2, 1, 0])

def checkPalindrome(ll):
    fast = slow = ll.head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
        
    while slow:
        top = stack.pop()
        
        if top != slow.value:
            return False
        
        slow = slow.next
        
    return True


print(checkPalindrome(ll))