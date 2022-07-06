# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:14:59 2022

@author: shrey
"""

'''
Problem statement:
    Convert a MaxHeap to a min Heap

Solution: 
    - Call minHeapify on all the parent nodes to convert each of them into 
    minHeaps iteratively
   
    
Complexity: 
    - Time complexity: O(n)
    - Space complexity: O(1) [No new memory?]
'''


def minHeapify(heap, index):
    
    # index of the two children
    left = 2*index + 1
    right = 2*index + 2
    
    # assigning the current parent as the parent as a placeholder
    smallest = index
    
    # check if the left child is present and if left child is smaller 
    if left < len(heap) and  heap[left] < heap[smallest]:
        smallest = left
    
    # check if the right child is present and if right child is smaller 
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right
        
    # Swap if the parent node isn't the smallest
    if smallest != index:
        temp = heap[smallest]
        heap[smallest] = heap[index]
        heap[index] = temp
        
        # After the swap, the smallest index now has to be minHeaped because it
        # is larger than it's children  
        minHeapify(heap, smallest)
        
    return heap
        

def convertMax(maxHeap):
    
    for index in range(len(maxHeap)//2, -1, -1):
        maxHeap = minHeapify(maxHeap, index)
        
    return maxHeap
        
maxHeap = [9, 4, 7, 1, -2, 6, 5]
print(convertMax(maxHeap))