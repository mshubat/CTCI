'''
Quick Sort Description

1. Pick a Pivot.
2. Put smaller items on its left and larger items on right.
3. Repeat for right and left sides of the Pivot untill sorted.

Time Complexity: O(nlogn)
Space Complexity: O(nlogn) * since the recusive calls must
                             keep track of the stack.
'''


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def quickSort(array):
    if len(array) > 1:
        pi = partition(array)
        return quickSort(array[0:pi]) + [array[pi]] + quickSort(array[pi+1:])
    else:
      return array


def partition(array):
    pivot = len(array) - 1

    i = 0
    j = 0

    while j != pivot:
        if array[j] <= array[pivot]:
            swap(array, i, j)
            i += 1

        j += 1

    swap(array, i, j)

    return i


if __name__ == "__main__":
    test = [999, 11, 22, 1, 3, 4, 2, 6, 55, 65, 22, 23, 1, 7, 33, 34, 222, -11]
    # return 1,2,3,4 or 1,2,4,3
    sorted = quickSort(test)
    print(sorted)

    test2 = [5,4,3,2,1,-1,-2,2,3,4,5]
    sorted = quickSort(test2)
    print(sorted)
