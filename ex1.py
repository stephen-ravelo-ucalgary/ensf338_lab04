class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    # Constructor
    def __init__(self, data):
        first_node = Node(data)
        self.head = first_node
        
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
        while(current_node.next):
            print(current_node.data)
            current_node = current_node.next
            if(current_node.next is None):
                print(current_node.data)

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
    def __init__(self, data):
        self.arr = [data]

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
This is because linked lists don't have instant access to a particular position in the list.
It needs to traverse through the list in order to find the element
'''