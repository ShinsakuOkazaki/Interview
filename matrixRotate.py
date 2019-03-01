#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:40:49 2019

@author: sinsakuokazaki
"""

def rotateImage(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            # left -> top
            matrix[first][i] = matrix[last-offset][first]
            #botton -> left
            matrix[last-offset][first] = matrix[last][last-offset]
            #right -> bottom
            matrix[last][last - offset] = matrix[i][last]
            #top -> right
            matrix[i][last] = top
    return True

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]