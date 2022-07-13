# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 13:18:41 2022

@author: shrey
"""
'''
Solution: 
    - Minheap for top half and maxheap for bottom half

'''


from heapq import heappush, heappop


class SlidingWindowMedian:
    
    def __init__(self):
        self._left = []
        self._right = []
        
    def find_sliding_window_median(self, nums, k):
        result = []
        
        for i, element in enumerate(nums):
            
            # add to left if this is the first element or if current element is 
            # smaller than the left array (heap)
            if not self._left or element <= -self._left[0]:
                heappush(self._left, -element)
            else:
                heappush(self._right, element)
                
            # Make length |left - right| <= 1
            self.rebalance_heaps()
              
            # Another condition can be i + 1 - k >=0 where i is index of current
            # element
            if len(self._left) + len(self._right) == k:
                if k%2 == 0:
                    result.append((self._left[0] + self._right[0])/2)
                else:
                    result.append(self._left[0])
                    
                # Element to be removed is the left end of the window
                element_delete = nums[i-k+1]
                if element_delete <= -self._left[0]:
                    self.remove(self._left, element_delete)
                else:
                    self.remove(self._right, element_delete)
                    
                self.rebalance_heaps()
                
        return result
    
    def rebalance_heaps(self):
        
        if len(self._left) > len(self._right) + 1:
            heappush(self._right, heappop(self._left))
        elif len(self._left) < len(self._right):
            heappush(self._left, heappop(self._right))
            
    def remove(self, heap, element):
        
        # replace the element to be removed by the last element in the heap
        
        idx = heap.index(element)
        heap[idx] = heap[-1]
        
        del heap[-1]
        
        # check if the index is still in heap
        if idx < len(heap):
        
            # now, if the replacement node is smaller than current parent, sift 
            # up, else, sift down
            
            # Resource: https://svn.python.org/projects/python/trunk/Lib/heapq.py
            # http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/heap-delete.html
            # https://en.wikipedia.org/wiki/Heap_%28data_structure%29
        
        
        

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()