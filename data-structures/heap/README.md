# Important equations and concepts

- A heap is a complete binary tree (i.e. it is a tree where each node has at most two children and the nodes at all levels are full, except for the leaf nodes which can be empty)

- Minheap: key(parent) <= key(child)


- Maxheap: key(parent) >= key(child)

- Heaps are mainly used for getting the smallest or largest element in O(1) time. They are also used to design Priority Queues. 

- Heaps can be represented as lists/arrays

	- For a parent at index k, the left child would be at 2k+1 position and the right child will be at 2k+2 position
	- The index of all the parent nodes will be <= floor(n-1/2), where n is the last index
	- The index of the first leaf node will be floor(n+1/2)., where n is the last index