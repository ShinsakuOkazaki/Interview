#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 21:14:04 2019

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
    
    
ll_1 = LinkedList([3, 1, 5, 9])
ll_2 = LinkedList([4, 6])
node1 = LinkedListNode(7)
node2 = LinkedListNode(2)
node3 = LinkedListNode(1)
ll_1.add_node(node1)
ll_1.add_node(node2)
ll_1.add_node(node3)
ll_2.add_node(node1)
ll_2.add_node(node2)
ll_2.add_node(node3)


def checkIntersection(ll_1, ll_2):
    if ll_1.tail is not ll_2.tail:
        return False
    length_1 = len(ll_1)
    length_2 = len(ll_2)
    
    current_1 = ll_1.head
    current_2 = ll_2.head
    
    if length_1 > length_2:
        move = length_1 - length_2
        for i in range(move):
            current_1 = current_1.next
    elif length_1 < length_2:
        move = length_2 - length_1
        for i in range(move):
            current_2 = current_2.next
            
    while current_1:
        if current_1 is current_2:
            return current_1
        current_1 = current_1.next
        current_2 = current_2.next

print(checkIntersection(ll_1, ll_2))
    
   
    
    
    


