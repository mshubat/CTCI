'''
Implement a function to check if a binary tree is
balanced. For the purpose of this question, a balanced
tree is defined to be a tree such that the heights of the
two subtrees of any node never differ by more than one.

Solution:

Could get the height of left and right subtrees. Starting
at the root and recursiively getting the heights of 
subtrees all the way down the tree. 

If heights differ by more than 1 then return False (ie.
the tree is not balanced) otherwise return True (the tree
is balanced.)
'''
from BST.binary_search_tree import binary_search_tree
from BST.node import node

def get_balanced(root):
    return is_balanced(root) != -1

def is_balanced(node):

    if node.getLeft():
        left_height = is_balanced(node.getLeft())
    else: 
        left_height = 0
    if node.getRight():
        right_height = is_balanced(node.getRight())
    else: 
        right_height = 0

    if left_height == -1 or right_height == -1:
        return -1

    if abs(left_height-right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    bst = binary_search_tree(5)
    print(bst.root.value)
    bst.insert_iteratively(3)
    bst.insert_iteratively(7)
    bst.insert_iteratively(8)
    bst.insert_iteratively(6)
    bst.insert_iteratively(4)
    bst.insert_iteratively(2)

    print(f"bst is balanced: {get_balanced(bst.root)}")

    bst = binary_search_tree(5)
    print(bst.root.value)
    bst.insert_iteratively(7)
    bst.insert_iteratively(8)
    bst.insert_iteratively(6)

    print(f"bst is balanced: {get_balanced(bst.root)}")
