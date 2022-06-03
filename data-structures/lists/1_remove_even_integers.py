# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 00:15:03 2022

@author: shrey
"""

#Problem statement: Remove all even numbers from the list

def remove_even(lst):

    # # using extra memory
    # ans = []

    # for num in lst:
    #     if num%2 != 0:
    #         ans.append(num)
    

    # using inplace memory 
    '''
    Intuition: using 2 pointers, one to track the current and other to 
    indicate the idex for modification
    '''

    curr = 0
    even = 0

    while curr < len(lst):
        if lst[curr] %2 != 0:
            lst[even] = lst[curr]
            even += 1
        curr +=1

    return lst[:even]