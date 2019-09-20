'''
Selection Sort Description:

Seletion sort is a simple yet inefficient algorithm.
"The Childs algorithm". It works by doing a linear scan
through the elements, selecting the smallest one, and
moving it to the front of the list. Repeating this process
untill the list is sorted.

Time Complexity: O(n^2) average and worst case
Space Complexity: O(1)
'''

# Helpers

def swap(arr, index1, index2):
    temp = arr[index2]
    arr[index2] = arr[index1]
    arr[index1] = temp
    return arr

def selectionSort(lst):

    start = 0

    while start<len(lst):
        smallest = lst[start]
        smallIndex = start

        for i in range(start, len(lst)):
            if lst[i]<smallest:
                smallest = lst[i]
                smallIndex = i
        swap(lst, start, smallIndex)
        start +=1
    return lst


if __name__ == "__main__":
    print("Selection Sort!")

    # test 1
    nums = [1,4,5,2,3,7,9,8,0,6]
    print(selectionSort(nums))

    # test 2
    nums = [11, 25, 12, 23, 73, 936]
    print(selectionSort(nums))
