# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:21:58 2022

@author: shrey
"""
# PROBLEM STATEMENT: MERGE TWO SORTED LISTS
'''
Solution: 
    - Get three pointers, one for each of the lists present and one for the 
    newly made final list
    - Check which of the pointed elements is smaller, add that to the final 
    list and increment the pointer forward
    - After finishing iteration over the smaller list, add the remaining 
    elements to the bigger list
    
Complexity: 
    - Time complexity: O(n+m) (as the lists were iterated over at least once)
    - Space complexity: O(n+m) (new list were created)
'''

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


'''
Solution 2: Merging in place 
    - Create two variables to track the current index of both lists
    - Compare elements at current indices, if the element of the 1st list is 
    bigger than the 2nd list, then insert the element of the second list at 
    the current position 
    - Increment both pointers
    - Else, increment only first pts
    
Compexity
    - Time complexity: O(n(n+m)) [shorter list traversal + insert function]
    
'''

def merge_arrays(lst1, lst2):
    ind1 = 0  # Creating 2 new variable to track the 'current index'
    ind2 = 0
    # While both indeces are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if(lst1[ind1] > lst2[ind2]):
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            ind1 += 1  # increment indices
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):  # Append whatever is left of list2 to list1
        lst1.extend(lst2[ind2:])
    return lst1


print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))