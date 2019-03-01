#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:37:22 2019

@author: sinsakuokazaki
"""
class LinkedListNode:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode
    
    def __str__(self):
        return str(self.value)

class LinkedList:
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
        return count
    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
            
    def add_multiple(self, values):
        for v in values:
            self.add(v)
            
    def add_node(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return self.tail
    
link = LinkedList(['A', 'B'])
node = LinkedListNode('C')
link.add_node(node)
link.add_multiple(['D', 'E'])
link.add_node(node)

def checkLoop(ll):
    fast = slow = ll.head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    
    if fast is None or fast.next is None:
        return False
    
    slow = ll.head 
    
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast

#def checkLoop(ll):
#    fast_pointer = ll.head.next.next
#    slow_pointer = ll.head.next
#    while fast_pointer is not slow_pointer:
#        fast_pointer = fast_pointer.next.next
#        slow_pointer = slow_pointer.next
#    slow_pointer = ll.head
#    while fast_pointer is not slow_pointer:
#        fast_pointer = fast_pointer.next
#        slow_pointer = slow_pointer.next
#    return fast_pointer 

#def checkLoop(ll):
#    table = []
#    current = ll.head
#    while current:
#        if hash(current) in table:
#            return True
#        table.append(hash(current))
#        current = current.next
#    return False
    
print(checkLoop(link))
    
    


