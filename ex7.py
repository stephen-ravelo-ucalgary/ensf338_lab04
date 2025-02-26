class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, node):
        node.next = self.head
        self.head = node
        if self.head.next is None:
            self.tail = node
    
    def insert_tail(self, node):
        self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def get_size(self):
        currNode = self.head
        size = 0
        while currNode is not None:
            currNode = currNode.next
            size += 1
        return size
    
    def get_element_at_position(self, pos):
        currNode = self.head
        for i in range(pos):
            currNode = currNode.next
        return currNode
    
    def reverse(self):
        newHead = None
        for i in range(self.get_size()):
            print(i)
            currNode = self.get_element_at_position(i)
            currNewNode = Node(currNode.data)
            if newHead is None:
                newHead = currNewNode
            else:
                currNewNode.next = newHead
                newHead = currNewNode
            self.head = newHead

if __name__ == "__main__":
    import timeit as tm
    import numpy as np
    import pandas as pd

    #ll = LinkedList()
    #length = 10
    #for i in range(length - 1, -1, -1):
    #    ll.insert_head(Node(i))
    
    #for i in range(length):
    #    print(ll.get_element_at_position(i).data)
    
    #ll.reverse()
    
    listLengths = [1000, 2000, 3000, 4000]
    averages = []

    for listLength in listLengths:
        ll = LinkedList()
        for i in range(listLength - 1, -1, -1):
            ll.insert_head(Node(i))
        time = tm.timeit(lambda: ll.reverse(), number=100)
        average = time/100
        averages.append(average)
        df_data = np.array([[listLength, average]])
        df = pd.DataFrame(df_data, columns=['list length', 'average time'])
        df['list length'] = np.int64(df['list length'])
        print(df.to_string(index=False))