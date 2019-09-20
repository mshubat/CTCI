'''
Q1.1
Implement an algorithm to determine if a string has all
unique characters. What if you cannot use additional data
structures?

If we can't use additional data structures, we can do the following:
1. Compare every char of the string to every other char
    Time: O(n^2)
    Space: O(1)
2. If we are allowed to change the array. Sort the chars 
and compare neighbouring chars.
    Time: O(nlogn)
    Space: Depends on sorting algorithm.

'''
import unittest
from collections import defaultdict

def is_unique(string):
    chars = defaultdict(int)

    for c in string:
        chars[c] += 1
        if chars[c] > 1:
            return False

    return True



if __name__ == "__main__":
    s1 = "abcdefg"

    isUnique = is_unique(s1)
    print(f"Should be True: {isUnique}")

    s2 = "abcdefghijklmnopqrstuvwxyza"
    isUnique = is_unique(s2)
    print(f"Should be False: {isUnique}")

    s3 = "hdhdhdhdhdhdhdhd"
    isUnique = is_unique(s3)
    print(f"Should be False: {isUnique}")

    s4 = "hdrha"
    isUnique = is_unique(s4)
    print(f"Should be False: {isUnique}")
