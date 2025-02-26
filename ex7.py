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
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_position(i)
            currNewNode = Node(currNode.data)
            if newHead is None:
                newHead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newHead

    def reverse_optimized(self):
        newHead = None
        currNode = self.head
        for i in range(self.get_size()):
            currNewNode = Node(currNode.data)
            currNode = currNode.next
            currNewNode.next = newHead
            newHead = currNewNode
        self.head = newHead

if __name__ == "__main__":
    import timeit as tm
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt
    from scipy.interpolate import interp1d

    DEBUG = False

    if DEBUG:
        ll = LinkedList()
        length = 10
        for i in range(length - 1, -1, -1):
            ll.insert_head(Node(i))
        
        ll.reverse_optimized()
        
        for i in range(length):
            print(ll.get_element_at_position(i).data)

    else:
        listLengths = [1000, 2000, 3000, 4000]
        averages = []
        averagesOptimized = []

        for listLength in listLengths:
            ll = LinkedList()
            for i in range(listLength - 1, -1, -1):
                ll.insert_head(Node(i))
            
            time = tm.timeit(lambda: ll.reverse(), number=100)
            average = time/100
            averages.append(average)

            time_optimized = tm.timeit(lambda: ll.reverse_optimized(), number=100)
            averageOptimized = time_optimized/100
            averagesOptimized.append(averageOptimized)

            df_data = np.array([[listLength, average, averageOptimized]])
            df = pd.DataFrame(df_data, columns=['list length', 'original', 'optimized'])
            df['list length'] = np.int64(df['list length'])
            print(df.to_string(index=False))

        fig = plt.figure(figsize=(1, 2))

        ax1 = fig.add_subplot(121)
        x_interp = np.linspace(np.min(listLengths), np.max(listLengths), 50)
        y_quadratic = interp1d(listLengths, averages, kind="quadratic")
        ax1.plot(x_interp, y_quadratic(x_interp), 'k', c='r', label="fitted curve")
        ax1.scatter(listLengths, averages, c='black', label="raw data")
        ax1.set_title('reversed()')
        ax1.set_xlabel('list length')
        ax1.set_ylabel('time')
        ax1.set_ylim(0)
        ax1.set_xlim(0)
        ax1.legend()

        ax2 = fig.add_subplot(122)
        slope, intercept = np.polyfit(listLengths, averagesOptimized, 1)
        line_values = [slope * x + intercept for x in listLengths]
        ax2.plot(listLengths, line_values, 'r', c='b', label="fitted line")
        ax2.scatter(listLengths, averagesOptimized, c='black', label="raw data")
        ax2.set_title('reversed() optimized')
        ax2.set_xlabel('list length')
        ax2.set_ylabel('time')
        ax2.set_ylim(0)
        ax2.set_xlim(0)
        ax2.legend()

        plt.show()
