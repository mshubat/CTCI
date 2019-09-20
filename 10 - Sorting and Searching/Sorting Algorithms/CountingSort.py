'''
Counting Sort Description:

(via GeeksforGeeks)
    Counting sort is a sorting technique based on keys 
    between a specific range. It works by counting the 
    number of objects having distinct key values (kind of 
    hashing). Then doing some arithmetic to calculate the 
    position of each object in the output sequence.

Note: works best when the range of nums to be sorted is
not much greater than the number of objects to be sorted.


Time Complexity: O(n+k) n # of elements, k is range of input
Space Complexity: O(n+k)
'''

# Implementation


def countingSort(nums):
    counts = [0]*(max(nums)+1)

    # Count occurences of elements in the array
    for i in nums:
        counts[i] += 1

    # Get cumulative count of elements
    for i in range(len(counts)-1):
        counts[i+1] += counts[i]

    sorted_nums = [0]*len(nums)
    for n in nums:
        sorted_nums[counts[n]-1] = n
        counts[n] -= 1

    return sorted_nums


# Test Cases
if __name__ == "__main__":
    print("Counting Sort Tests")

    # test 1
    result = countingSort([4, 3, 10, 2, 3, 4, 5, 8, 7])
    print(result)

    result = countingSort([9, 8, 7, 6, 10, 5, 4, 3, 2, 1, 0])
    print(result)
