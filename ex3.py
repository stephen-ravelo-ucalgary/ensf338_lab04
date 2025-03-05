# Question 1
#   In the C implementation of Python lists provided in the lists.c file, when appending to the list 
#   (dynamic array), when it is full, the dynamic array grows by over-allocating memory when a new 
#   element is appended. In the list_resize function in the lists.c file, the line: 
#   new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;
#   This line shows that when the list needs to be resized, the new allocated size is calculated by 
#   adding newsize >> 3 which is the equivalent to newsize / 8 and 6. Adding this to (size_t)newsize 
#   results in an increase of 12.5%. So the growth factor is 1.125.

import sys
import time
import timeit
import matplotlib.pyplot as plt

def testListChange():
    lst = []
    prevSize = sys.getsizeof(lst)
    capacityChange = []
    print(f"Initial capacity: {prevSize} bytes (0 elements)")
    for i in range(64):
        lst.append(i)
        newSize = sys.getsizeof(lst)
        
        if newSize != prevSize:
            print(f"At {len(lst)} elements: capacity changed from {prevSize} to {newSize} bytes")
            capacityChange.append((len(lst), newSize))
            prevSize = newSize
    
    return capacityChange          

def trigExpansion(s):
    lst = list(range(s))
    lst.append(0)


def noTrigExpansion(s):
    lst = list(range(s - 1))
    lst.append(0)


if __name__ == "__main__":
    capacityChange = testListChange()
    
    if capacityChange:
        s = capacityChange[0][0]
    else:
        s = 4
        
    timesTrigger = timeit.repeat(lambda: trigExpansion(s), repeat=1000, number=1)
    timesNoTrigger = timeit.repeat(lambda: noTrigExpansion(s), repeat=1000, number=1)
    
    avgTimesTrigger = sum(timesTrigger) / len(timesTrigger)
    avgTimesNoTrigger = sum(timesNoTrigger) / len(timesNoTrigger)
    
    print(f"\nAverage time for append causing expansion (S -> S+1): {avgTimesTrigger:.10f} seconds")
    print(f"Average time for append without expansion (S-1 -> S): {avgTimesNoTrigger:.10f} seconds")
    
    plt.figure(figsize=(10, 5))
    plt.hist(timesTrigger, bins=30, alpha=0.7, label="Append causing expansion (S -> S+1)")
    plt.hist(timesNoTrigger, bins=30, alpha=0.7, label="Append without expansion (S-1 -> S)")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Timing Distribution for Append Operations (1000 measurements)")
    plt.legend()
    plt.show()

# Quesion 5
#   The histogram for appends that trigger expansion typically show higher and more variable times.
#   This is likely due to the operation needing to allocate new memory and copying existing elements 
#   to the newly allocated memory. The appends that do not trigger an expansion should be faster and 
#   have less variation in their times, as they do not have to allocate new memory or copy exisiting 
#   elements.