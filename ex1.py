import timeit
from matplotlib import pyplot as plt
import numpy as np
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None
        
    # Linked List Methods
    def headInsert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def tailInsert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node
    def printLList(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    # Linked List Binary Search Method
    def middle(self, start, last):
        if start is None:
            return None
        if start == last:
            return start
        slow = start
        fast = start.next

        while fast != last:
            fast = fast.next
            slow = slow.next
            if fast != last:
                fast = fast.next
        return slow

    def binary_search(self, num):
        start = self.head
        last = None

        while True:
            mid = self.middle(start, last)
            if mid is None:
                return False
            if mid.data == num:
                return True
            elif start == last:
                break
            elif mid.data < num:
                start = mid.next
            elif mid.data > num:
                last = mid
        return False

# Array Class
class Array:
    # Constructor
    def __init__(self):
        self.arr = None

    # Array Methods
    def tailInsert(self, data):
        if self.arr is None:
            self.arr = [data]
            return
        self.arr.append(data)
    def printArray(self):
        for i in range(len(self.arr)):
            print(self.arr[i])

    # Array Binary Search Method
    def binary_search(self, num):
        low = 0
        high = len(self.arr) - 1
        mid = 0

        while low <= high:
            mid = (high + low) // 2

            if self.arr[mid] < num:
                low = mid + 1
            elif self.arr[mid] > num:
                high = mid - 1
            else:
                return mid
        return -1

'''
Question 4 Answer
The complexity of binary search for linked lists is O(n), which is the same for linear search.
This is because linked lists don't have instant access to a particular position in the list, it needs
to traverse through the list in order to find the element in the middle which has complexity O(n).
The O(n) complexity then dominates binary search's complexity of O(logn).
'''

x_values = [1000, 2000, 4000, 8000]
bin_search_llist = []
bin_search_arr = []
# Timing of binary search on a linked list
for i in x_values:
    linked_list = LinkedList()
    # x_list for choosing a random int to search
    x_list = list(range(1, i + 1))
    # create linked list
    for y in range(1, i + 1):
        linked_list.tailInsert(y)
    elapsed_time = 0
    for x in range(0, 100):
        elapsed_time += timeit.timeit(lambda : linked_list.binary_search(random.choice(x_list)), number = 1)
    elapsed_time_avg = elapsed_time / 100
    bin_search_llist.append(elapsed_time_avg)

# Timing of binary search on an array
for i in x_values:
    arr = Array()
    x_list = list(range(1, i + 1))
    for y in range(1, i + 1):
        arr.tailInsert(y)
    elapsed_time = 0
    for x in range(0, 100):
        elapsed_time += timeit.timeit(lambda : arr.binary_search(random.choice(x_list)), number = 1)
    elapsed_time_avg = elapsed_time / 100
    bin_search_arr.append(elapsed_time_avg)

# Plotting
x_values = np.array(x_values)
bin_search_llist = np.array(bin_search_llist)
bin_search_arr = np.array(bin_search_arr)

fit_bin_llist = np.polyfit(x_values, bin_search_llist, deg = 2)
fit_bin_arr = np.polyfit(x_values, bin_search_arr, deg = 2)

x_smooth = np.linspace(1000, 8000, 500)
y_llist_smooth = np.polyval(fit_bin_llist, x_smooth)
y_arr_smooth = np.polyval(fit_bin_arr, x_smooth)

plt.scatter(x_values, bin_search_llist, label = "Linked List", marker = 'o', color = 'b')
plt.scatter(x_values, bin_search_arr, label = "Array", marker = 'o', color = 'r')
plt.plot(x_smooth, y_llist_smooth, label = "Linked List Interpolated", color ='b')
plt.plot(x_smooth, y_arr_smooth, label = "Array Interpolated", color = 'r')

plt.title("Binary Search Average Case")
plt.xlabel("Size (n)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
