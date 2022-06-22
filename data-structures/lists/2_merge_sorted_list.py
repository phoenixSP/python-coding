# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:21:58 2022

@author: shrey
"""

def merge_lists(lst1, lst2):
    
    p1 = 0
    p2 = 0
    p3 = 0
    res = [0]*(len(lst1) + len(lst2))
    
    while p1 < len(lst1) and p2 < len(lst2):
        if lst1[p1] < lst2[p2]:
            res[p3] = lst1[p1]
            p1 += 1
        else:
            res[p3] = lst2[p2]
            p2 += 1
        p3 += 1
        
    while p1 < len(lst1):
        res[p3] = lst1[p1]
        p1 += 1
        p3 += 1
        
    while p2 < len(lst2):
        res[p3] = lst2[p2]
        p2 += 1
        p3 += 1

    return res