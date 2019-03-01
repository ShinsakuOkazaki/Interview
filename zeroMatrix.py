#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:59:57 2019

@author: sinsakuokazaki
"""
#space O(N^2)
def zeroMatrix(matrix):
    row = [None] * len(matrix)
    column = [None] * len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True
    for i in range(len(row)):
        if row[i]: nullifyColumn(matrix, i)
    
    for j in range(len(column)):
        if column[j]: nullifyRow(matrix, j)
    return matrix

def nullifyRow(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0

def nullifyColumn(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


m1 = [[0,1,2],
      [3,4,5],
      [6,7,8],
      [9,10,11]]

def setZeros(matrix):
    rowHasZero = False
    colHasZero = False
    #check if first row has a zero
    for j in range(len(len(matrix[0]))):
        if matrix[0][j] == 0:
            rowHasZero = True
            break
    #check if first column has a zero
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colHasZero = True
            break
    #check for zeros in the rest of the array
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    #Nullify rows based on svalues in first column
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            nullifyRow(matrix, i)
    #Nullify columns based on values in first row
    for j in range(len(matrix[0])):
        if matrix[0][j] == 0:
            nullifyColumn(matrix, 0)
            
    #Nullify first row
    if rowHasZero:
        nullifyRow(matrix, 0)
    #Nullify second column
    if colHasZero:
        nullifyColumn(matrix, 0)