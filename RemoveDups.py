#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:08:56 2019

@author: sinsakuokazaki
"""

class Node:
    def __init__(self, data = None ,next_node = None):
        self.data = data
        self.next_node = next_node
        
    def append(self, data):
        end = Node(data)
        while self.next_node != None:
            self = self.next_node
        self.next_node = end
        
    def __str__(self):
        return str(self.data)
    
node = Node(1)
node.append(4)
node.append(3)
node.append(0)
node.append(1)
node.append(4)
node.append(1)

#O(n) time
def deleteDups(n):
    s = set()
    previous = Node()
    while n != None:
        if n.data in s:
            previous.next_node = n.next_node
        else:
            s.add(n.data)
            previous = n
        n = n.next_node
        
#O(1) space and O(N^2)
def deleteDups2(head):
    current = head
    while current:
        runner = current
        while runner.next_node:
            if runner.next_node.data == current.data:
               runner.next_node = runner.next_node.next_node
            else:
                runner = runner.next_node
        current.next_node

