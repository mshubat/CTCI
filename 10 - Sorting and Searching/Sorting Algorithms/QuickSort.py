'''
Quick Sort Description

1. Pick a Pivot.
2. Put smaller items on its left and larger items on right.
3. Repeat for right and left sides of the Pivot untill sorted.

Time Complexity: O(nlogn)
Space Complexity: O(nlogn) * since the recusive calls must
                             keep track of the stack.
'''


def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp


def quickSort(array, start, end):

    if start < end:
        pi = partition(array, start, end)

        quickSort(array, pi+1, end)
        quickSort(array, start, pi-1)


def partition(array, start, end):
    pivot = end

    i = -1
    j = 0

    while j != pivot:
        if array[j] <= array[pivot]:
            i += 1
            swap(array, i, j)

        j += 1

    swap(array, i+1, j)

    return i+1


if __name__ == "__main__":
    test = [999, 11, 22, 1, 3, 4, 2, 6, 55, 65, 22, 23, 1, 7, 33, 34, 222, -11]
    # return 1,2,3,4 or 1,2,4,3
    quickSort(test, 0, len(test)-1)
    print(test)
