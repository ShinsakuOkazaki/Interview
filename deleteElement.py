#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 18:07:18 2019

@author: sinsakuokazaki
"""

class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
        
    def append(self, data):
        end = Node()
        end.data = data
        while self.next_node:
            self = self.next_node
        self.next_node = end
    def __str__(self):
        return str(self.data)
    
node = Node("a")
node.append("b")
node.append("c")
node.append("d")
node.append("e")
node.append("f")
node.append("g")

#delete an element in middle of linked list
def deleteElement(node):
    if node == None or node.next_node == None:
        return False
    
    nextNode = node.next_node
    node.data = nextNode.data
    node.next_node = nextNode.next_node
    
result = deleteElement(node.next_node)

while node.next_node:
    print(node)
    node = node.next_node