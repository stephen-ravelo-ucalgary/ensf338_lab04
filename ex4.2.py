import timeit
import matplotlib.pyplot as plt

def linearSearch(arr, key):
    for x in arr:
        if x == key:
            return True
    return False

def binarySearch(arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2
        
        if (key == arr[mid]):
            return True
        elif (key < arr[mid]):
            return binarySearch(arr, first, mid - 1, key)
        elif (key > arr[mid]):
            return binarySearch(arr, mid + 1, last, key)
        
        return False

if __name__ == "__main__":
    arr = list(range(1000))
    key = 999
    first = 0
    last = len(arr) - 1
    
    linearTimes = timeit.repeat(lambda: linearSearch(arr, key), repeat=100, number=1)
    binaryTimes = timeit.repeat(lambda: binarySearch(arr, first, last, key), repeat=100, number=1)

    avgLinear = sum(linearTimes) / len(linearTimes)
    avgBinary = sum(binaryTimes) / len(binaryTimes)
    print(f"Average time for linear search (O(n)): {avgLinear:.10f} seconds")
    print(f"Average time for binary search (O(log n)): {avgBinary:.10f} seconds")

    # Plot histograms for both sets of timings
    plt.figure(figsize=(10, 5))
    plt.hist(linearTimes, bins=20, alpha=0.7, label="Linear Search (O(n))")
    plt.hist(binaryTimes, bins=20, alpha=0.7, label="Binary Search (O(log n))")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency")
    plt.title("Timing Distribution for Search Algorithms (100 measurements)")
    plt.legend()
    plt.show()
# Question 3
#   The inefficient implementation of searching a sorted array is a linear search.
#   The efficient implementation of searching a sorted array is a binary search.

# Question 4
#   The worst case complexity of linear search is O(n) which occurs when the key is either the last 
#   element of the array of the key does not exist within the array.
#   The worst case complexity of binary search is O(log n), since the search space is halved after each
#   iteration.

