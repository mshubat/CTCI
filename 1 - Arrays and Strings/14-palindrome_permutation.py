'''
Givien a string, write a function to check if it is a 
permutation of a palindrome. A Palindrome is a word or 
phrase which is the same forwards and backwards. A 
Permutation is a rearrangement of letters. The palindrome
does not need to be limited to just dictionary words.
'''
from collections import defaultdict

def is_pal_perm(word):
    s = word.replace(" ", "") # remove any spaces
    s = s.lower()

    d = defaultdict(int) # store letter counts

    for c in s:
        d[c] += 1

    tot_chars = len(s)
    len_is_odd = tot_chars%2 == 1

    if len_is_odd:
        max_allowed = 1
    else: 
        max_allowed = 0

    for k,v in d.items():
        if v%2 != 0:
            max_allowed -= 1
        if max_allowed < 0:
            return False

    return True

if __name__ == "__main__":
    print(is_pal_perm("abccba")) # True

    print(is_pal_perm("defde")) # True

    print(is_pal_perm("Tact Coa"))

    print(is_pal_perm("abde"))