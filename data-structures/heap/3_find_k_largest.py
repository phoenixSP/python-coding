# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 12:38:19 2022

@author: shrey
"""

'''
Problem statement: Find k largest element in a list

Solution:
    - Create a minheap to keep track of the current top k elements
    - Process each element of the input array. If element > smallest element in 
    the min heap, pop the smallest and add current elememnt
    
Time complexity:
    - Adding k elements O(k)
    - Processing rest of the elements and adding them to the minHeap O((n-k)logk)
    - Overall: O(nlogk)
    
Space complexity:
    - O(k) for storing the k elements

'''

import heapq

def minHeap(heap, element, k):
    
    if len(heap) < k:
        heapq.heappush(heap, element)
    elif element > heap[0]:
        heapq.heappushpop(heap, element)
        
    return heap


def findKLargest(lst, k):
    
    heap = []
    
    for element in lst:
        heap = minHeap(heap, element, k)
        
    return heap

arr = [1, 5, 6, 2, 3]
print(findKLargest(arr, 3))
        