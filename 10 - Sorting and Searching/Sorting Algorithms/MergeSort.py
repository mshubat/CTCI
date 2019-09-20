'''
Merge Sort Description:

Merge sort divides the array in half and sorts each of
those halves, then merges them back together. Each half
has the same sorting algorithm applied to it until each
half contains only one number. The merge does the "heavy
lifting".

Time Complexity: O(n*logn)
Space Complexity: O(n) [Depends]
'''


def mergeSort(arr, low, high):

    if high > low:
        former = mergeSort(arr[0:len(arr)//2], 1, len(arr)//2)
        ladder = mergeSort(arr[len(arr)//2:len(arr)], 1, len(arr)-len(arr)//2)
        return merge(former, ladder)
    else:
        return arr


def merge(former, ladder):
    combined = []
    former_empty = False
    ladder_empty = False
    fi = 0
    li = 0

    while (not former_empty and not ladder_empty):
        if former[fi] < ladder[li]:
            combined.append(former[fi])
            fi += 1
            if fi == len(former):
                former_empty = True
        else:
            combined.append(ladder[li])
            li += 1
            if li == len(ladder):
                ladder_empty = True

    if former_empty:
        while li < len(ladder):
            combined.append(ladder[li])
            li += 1
    elif ladder_empty:
        while fi < len(former):
            combined.append(former[fi])
            fi += 1

    return combined


if __name__ == "__main__":
    items = [3,6,4,7,5,1,2,8,10,9]
    print(items)

    items = mergeSort(items, 1, len(items))
    print(items)