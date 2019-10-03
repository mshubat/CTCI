'''
Given a sorted (increasing  order) array with unique
integer elements, write an algorithm to create a binary
search tree with minimal height.
'''
from BST.binary_search_tree import binary_search_tree

def insert_middle(array, bst):
    mid = len(array)//2  # find midpoint
    bst.insert(array[mid])
    
    if len(array) == 1:
        return bst
    elif len(array) == 2:
        bst.insert(array[0])
        return bst

    insert_middle(array[0:mid], bst)
    insert_middle(array[mid+1:], bst)

def bst_from_sorted_arr(array):
    mid = len(array)//2 # find midpoint
    bst = binary_search_tree(array[mid])

    if len(array) == 1:
        return bst

    insert_middle(array[0:mid], bst)
    insert_middle(array[mid+1:], bst)

    return bst

if __name__ == "__main__":
    array = [1,4,8,10,14]

    bst = bst_from_sorted_arr(array)
    print("InOrder:")
    bst.inOrder(bst.root)
    print()
    print("PreOrder:")
    bst.preOrder(bst.root)
    print()
    print("PostOrder:")
    bst.postOrder(bst.root)
    print()