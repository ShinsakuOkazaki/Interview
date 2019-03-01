#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:02:24 2019

@author: sinsakuokazaki
"""
class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    def append(self, data):
        end = Node(data)
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

#recusive function to pint out
def getResult(head, k):
    result = []
    printKthToLast(head, k,result)
    return result
        

def printKthToLast(head, k, result):
    if not head:
        return 0
    index = printKthToLast(head.next_node, k, result) + 1
    if index == k:
        while head.next_node:
            result.append(head.data)
            head = head.next_node
        result.append(head.data)
    return index

result = getResult(node, 3)