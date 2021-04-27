
# Helpers
def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

# Bubble Sort
def bubble_sort(nums):
  end = len(nums)-1

  while (end > 0):
    # sort
    for i in range(end):
      if (nums[i] > nums[i+1]):
        swap(nums, i, i+1)
    end -= 1

  return nums

# Selection Sort
def selection_sort(nums):
  end = len(nums) - 1

  while (end > 0):
    i = 0
    while (i < end):
      if (nums[i] > nums[end]):
        swap(nums, i, end)
      i += 1
    end -= 1

  return(nums)

# Insertion Sort
def insertion_sort(nums):
  i = 1
  while (i < len(nums)):
    j = i - 1
    temp = nums[i]
    while (j >= 0 and nums[j] > temp):
      nums[j+1] = nums[j]
      nums[j] = temp
      j -= 1
    i += 1
  return nums

# Quick Sort
def quick_sort(nums):
  pass


# Merge Sort
def merge_sort(nums):
  pass

# Counting Sort
def counting_sort(nums):
  pass


# Tests
if __name__ == "__main__":

  test1 = [4,5,3,2,6,1]
  test2 = [4,500,3,22,6,13]
  test3 = [4,500,3,22,6,13,2,3,4,2,43,888,8888]
  test4 = [1,2,3,4,5,6]
  test5 = [6, 5, 4, 3, 2, 1]

  print(insertion_sort(test1))

  # Test 1
  try:
    assert(bubble_sort(test1.copy()) == sorted(test1.copy()))
    assert(selection_sort(test1.copy()) == sorted(test1.copy()))
    assert(insertion_sort(test1.copy()) == sorted(test1.copy()))
    print("test 1 passed")
  except:
    print("test 1 failed")

  # Test 2
  try: 
    assert(bubble_sort(test2.copy()) == sorted(test2.copy()))
    assert(selection_sort(test2.copy()) == sorted(test2.copy()))
    assert(insertion_sort(test2.copy()) == sorted(test2.copy()))
    print("test 2 passed")
  except:
    print("test 2 failed")

  # Test 3
  try: 
    assert(bubble_sort(test3.copy()) == sorted(test3.copy()))
    assert(selection_sort(test3.copy()) == sorted(test3.copy()))
    assert(insertion_sort(test3.copy()) == sorted(test3.copy()))
    print("test 3 passed")
  except:
    print("test 3 failed")

  # Test 4
  try: 
    assert(bubble_sort(test4.copy()) == sorted(test4.copy()))
    assert(selection_sort(test4.copy()) == sorted(test4.copy()))
    assert(insertion_sort(test4.copy()) == sorted(test4.copy()))
    print("test 4 passed")
  except:
    print("test 4 failed")

  # Test 5
  try: 
    assert(bubble_sort(test5.copy()) == sorted(test5.copy()))
    assert(selection_sort(test5.copy()) == sorted(test5.copy()))
    assert(insertion_sort(test5.copy()) == sorted(test5.copy()))
    print("test 5 passed")
  except:
    print("test 5 failed")