## Exercise 6

### Question 1
Arrays Advantages:
- Fast access using index
- Elements are stored contiguously, reduces memory fragmentation
- Can be used to store different kinds of data types

Arrays Disadvantages:
- Fixed size when created, not great when size needs to be changed multiple times throughout the program
- Since arrays are stored contiguously, large arrays might be unable to fit in available memory leading to crashes

Array Task Complexities:
- Insertion: O(n)
- Delete: O(n)

Singly Linked List Advantages:
- Size can be dynamically changed, good when program changes its size multiple times in the program
- since linked lists are not stored contiguously, large linked lists cause no memory problems

Singly Linked List Disadvantages:
- uses more memory than arrays since it needs a pointer pointing to the next node
- finding an element in the list is more time consuming than arrays
- uses more memory because of its pointers

Singly Linked List Task Complexities:
- Head Insertion: O(1)
- Tail Insertion: O(n)
- Head Deletion: O(1)
- Tail Deletion: (n)

### Question 2
Assuming that we find get an element at a certain index and replacing it to a new index, we can consider two cases:
1. If starting position is greater than the new position. We retrieve the element at the starting position then shift all elements that are within the range of startingpos - newpos to the right, leaving an open space for the element we are replacing.
2. If starting position is less than the new position. We retrieve the element at the starting position then shift all elements that are within the range of newpos - startingpos to the left, leaving an open space for the element we are replacing.

Both implementations will have a complexity of O(n).

### Question 3
Doubly Linked List Insertion Sort

Since a doubly linked list has next and previous pointers for each node, an implementation of insertion sort is easy to achieve. In each iteration, a node's value is compared with the value of the node to its left. If the value is smaller than the current value, the node is moved by adjusting its pointers. The next and previous pointers are updated, along with the nodes on both sides to ensure proper connectivity between all the nodes. After all iterations, the doubly linked list is then sorted.

Doubly Linked List Merge Sort

Since merge sort involves the idea of splitting the list into halves recursively, it is also possible to implement this algorithm using a doubly linked list since the nodes are easily moved around because of their next and previous pointers. Once the list is divided into sub-lists of only one node, they are then merged together. They are merged by comparing the values of the nodes, adjusting the pointers in the process to sort them. The process is repeated until all sub-lists are merged into one sorted list.

### Question 4
Insertion Sort

The time complexity of insertion sort on a doubly linked list is $O(n^2)$ because the list has to be traversed, then the nodes are compared with a certain number of nodes to its left. The complexity is the same when insertion sort is applied to a regular array. The key difference is that the nodes are not shifted but instead their pointers are adjusted unlike arrays where its elements are shifted.

Merge Sort

The time complexity of merge sort on a doubly linked list is O(n logn) because the list is divided into halves recursively, this process has O(log n) complexity. Merging these nodes back together then takes O(n), as each node's pointers must be adjusted to form the sorted list. These complexities are multiplied since it greatly depends on the size of the input when the sub-lists are only going to consist of one node. The complexity is the same when merge sort is applied to a regular array. The key difference, like with insertion sort, is that the nodes are not shifted but their pointers are adjusted instead. As a result, no extra memory is needed unlike arrays, where additional memory space is needed during merging.
