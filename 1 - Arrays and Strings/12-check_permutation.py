'''
Given two strings, write a method to determine if one is 
a permutation of the other.

Time: O(n)
Space: O(n)

Alternatively, (after checking for equal length) we can 
sort the strings and compare each char one after the 
other, ensuring each of them is equivalent.

Time: O(nlogn)
'''
from collections import defaultdict

def getCharMap(s):
    chars = defaultdict(int)
    for c in s:
        chars[c]+=1
    return chars

def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False

    d1 = getCharMap(string1)
    d2 = getCharMap(string2)

    for c in string1:
        if d1[c] != d2[c]:
            return False
    return True

if __name__ == "__main__":
    s1 = "abcdefg"
    s2 = "zersfgs"

    result = check_permutation(s1,s2)
    if result:
        print("s1 and s2 are permutations! :)")
    else:
        print("s1 and s2 are NOT permutations :(")

    s1 = "abcdefg"
    s2 = "gfebcad"

    result = check_permutation(s1, s2)
    if result:
        print("s1 and s2 are permutations! :)")
    else:
        print("s1 and s2 are NOT permutations :(")

    s1 = "pooperscooper"
    s2 = "scooperpooper"

    result = check_permutation(s1, s2)
    if result:
        print("s1 and s2 are permutations! :)")
    else:
        print("s1 and s2 are NOT permutations :(")
