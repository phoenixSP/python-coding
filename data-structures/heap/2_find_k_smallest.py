# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 10:20:13 2022

@author: shrey
"""
'''
Problem statement: Find k smallest elements in an array

Solution:
    - Create a maxHeap to store the 5 smallest elements
    - For each element in the input array, check if it is smaller than the 
    largest element. If yes, add it to the heap. Else, discard
    
Compexity: 
    - Time complexity: 
        - Adding k elements: O(k) [similar to heapification, since length is 
        dynamic] < O(klogk)
        - Processing the rest of the elements: O((n-k)log k)
        - Overall time complexity: O(klogk + (n-k)logk) = O(nlogk)
        
    - Space complexity: 
        - O(k) as we need to store k elements

'''



import heapq

# Python's implementation of heapq is a minHeap, hence we need to make changes 
# to use it as a maxHeap

def maxHeap(heap, k, element):
    
    if len(heap) < k:
        heapq.heappush(heap, -element)
    elif element < -heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, -element)
    return heap


def findKSmallest(lst, k):
    # Write your code here
    heap = []
    
    for element in lst:
        heap = maxHeap(heap, k, element)
        
    res = []
    while heap:
        res.append(-heapq.heappop(heap))
        
        
    return res


arr = [1, 5, 6, 2, 3]
print(findKSmallest(arr, 3))

# Optimal solution is given by quick select algorithm with average case complexity of O(n)
# Link: https://www.geeksforgeeks.org/quickselect-algorithm/