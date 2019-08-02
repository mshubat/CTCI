'''
Bubble Sort Description:

In bubble sort, we start at the beginning of the array 
and swap the first two elements if the first is greater
than the second. Then we proceed to the next pair, and 
so on. This process is repeated for multiple sweeps of 
the array until it is sorted.

Time Complexity: O(n^2) average and worst case
Space Complexity: O(1)
'''

# Helpers

def swap(arr, index1, index2):
    temp = arr[index2]
    arr[index2] = arr[index1]
    arr[index1] = temp
    return arr 

# Implementation

def bubbleSort(arr):
    s = len(arr)-1
    while (s>0):
        for i in range(s):
            if arr[i]>arr[i+1]:
                swap(arr, i, i+1)
        s-=1
    
    print (arr)


# Test Cases
if __name__ == "__main__":
    print("Bubble Sort Tests")

    # test 1
    bubbleSort([2,3,4,5,8,7,10,4,11,1])

    # test 2
    bubbleSort([22,1,2,6,3,22,333,4,667,3,11,33,44,55])
