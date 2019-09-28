import math 

def binary_search(nums, x):

    if len(nums) == 0  or (len(nums) == 1 and nums[0] != x):
        print ("x not in list")
        return -math.inf

    end = len(nums)
    mid = len(nums)//2
    
    if x == nums[mid]:
        return mid
    elif x > nums[mid]:
        return(binary_search(nums[mid+1:end], x) + mid+1)
    elif x < nums[mid]:
        return(binary_search(nums[0:mid], x))


if __name__ == "__main__":
    nums = [1,2,5,6,22,33,34,50,100,120,122,300]

    print(f"Should return 3: {binary_search(nums, 6)}")
    print(f"Should return -inf: {binary_search(nums, 3010)}")
    print(f"Should return 11: {binary_search(nums, 300)}")
    print(f"Should return 10: {binary_search(nums, 122)}")
    print(f"Should return 1: {binary_search(nums, 2)}")
    
