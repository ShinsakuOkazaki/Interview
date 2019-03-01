#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 15:05:24 2019

@author: sinsakuokazaki
"""

from linkedList import LinkedList

def sumList(ll_1, ll_2):
    n1, n2 = ll_1.head, ll_2.head
    ll_result = LinkedList()
    carry = 0
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result +=n2.value
            n2 = n2.next
            
        ll_result.add(result % 10)
        carry = result // 10
    
    if carry:
        ll_result.add(carry)
    return ll_result


def followUp(ll_1, ll_2):
    if len(ll_1) < len(ll_2):
        for i in range(len(ll_2) - len(ll_1)):
            ll_1.add_to_beginnig(0)
    else:
        for i in range(len(ll_1) - len(ll_2)):
            ll_2.add_to_beginning(0)
    
    n1, n2 = ll_1.head, ll_2.head
    result = 0
    while n1 and n2:
        result = result * 10 + n1.value + n2.value
        
    ll_result = LinkedList()
    ll_result.multiple([int(i) for i in str(result)])
    return ll_result
    
'''
def sumList(ll_1, ll_2):
    ll_result = LinkedList()
    carry = 0
    for l1, l2 in zip(ll_1, ll_2):
        if carry:
            num = l1.value + l2.value + carry
        else:
            num = l1.value + l2.value
        if num // 10:
            carry = num // 10
            ll_result.add(num % 10)
        else:
            ll_result.add(num)
    return ll_result
'''
        
"""
def sumList(ll_1, ll_2):
    result_1 = 0
    result_2 = 0
    for i, j in zip(ll_1 ,range(len(ll_1))):
        result_1 += i.value * 10 ** j   
    for i, j in zip(ll_2, range(len(ll_2))):
        result_2 += i.value * 10 ** j
       
    result = result_1 + result_2
    ll_result = LinkedList()

    for k in range(len(str(result))-1, -1 , -1):
         num = result // 10 ** k
         ll_result.add_to_beginning(num)
         result = result - num * 10 ** k
    return ll_result
"""
ll_1 = LinkedList()
ll_2 = LinkedList()
ll_1.add_multiple([7,1,6,1])
ll_2.add_multiple([5,9,1])

result_list = sumList(ll_1, ll_2)
result_num = 0

for i, j in zip(result_list, range(len(result_list))):
    result_num += i.value * 10 ** j


print(result_list)
print("That is", result_num)


