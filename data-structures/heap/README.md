# Important equations and concepts

- A heap is a complete binary tree (i.e. it is a tree where each node has at most two children and the nodes at all levels are full, except for the leaf nodes which can be empty)

- Minheap: key(parent) <= key(child)


- Maxheap: key(parent) >= key(child)

- Heaps are mainly used for getting the smallest or largest element in O(1) time. They are also used to design Priority Queues. 

- Heaps can be represented as lists/arrays

	- For a parent at index k, the left child would be at 2k+1 position and the right child will be at 2k+2 position
	- The index of all the parent nodes will be <= floor(n-1/2), where n is the last index
	- The index of the first leaf node will be floor(n+1/2)., where n is the last index


## Max Heap

### Insertion in a max heap
- Create a new child at the end of the heap
- Place the new key at that node
- Then restore the heap property by swapping the parent and child values, if the parent is smaller than the child key. This is called "percolating up".
- Continue to percolate up till the heap property is restored
- *Time complexity*: O(log(n)), because that is the maximum number of nodes that would have to be traversed and/or swapped

### Removing the maximum from a max heap
- Delete the root node
- Move the key of the last child at the last level to the root
- Compare the key with its children and if the root key is smaller, swap values with the smallest child. This is called "Max Heapifying"
- Continue to max heapify until heap property is restored 
- *Time complexity*: O(log(n)), because that is the maximum number of nodes that would have to be traversed and/or swapped

## Get Maximum
- Get the first element
- *Time complexity*: O(1)

## Build a Heap 
- Perform Max Heapify operation at each index starting from the last index of the list building a heap
- *Time complexity*: O(n)
	- The number of comparisons for a particular node at height h is O(h)
	- The number of nodes at height h is at most ceil(n/2^(h+1)) = n_node(h)
	- The time complexity is summation of n_node(h)*O(h) where h is from 0 to log(n)


