'''
Implement a function to check if a binary tree is a 
binary search tree.

Method 1: 
In order traversal of the tree, checking that each element
which is printed is larger than the element before it. If 
the items are in order than the ordered property of the 
tree is correct.
'''
from BST.binary_search_tree import binary_search_tree
from BST.node import node

def isBST(root):
    lst = inOrderToList(root)

    for i in range(len(lst)-1):
        #print(f'{lst[i]} > {lst[i+1]} = {lst[i] > lst[i+1]}')
        if lst[i] > lst[i+1]:
            return False

    return True

def inOrderToList(node, list=[]):

    if node.getLeft():
        inOrderToList(node.getLeft())

    list.append(node.getValue())

    if node.getRight():
        inOrderToList(node.getRight())

    return list

def isBST_v2(root, prev=None):

    if root.getLeft():
        prev = isBST_v2(root.getLeft(), prev)
    
    if prev == False:
         return False

    if prev and root.getValue() < prev:
        return False
    
    prev = root.getValue()

    if root.getRight():
        prev = isBST_v2(root.getRight(), prev)
    
    return prev

    



if __name__ == "__main__":
    bst = binary_search_tree(5)
    print(bst.root.value)
    bst.insert_iteratively(3)
    bst.insert_iteratively(7)
    bst.insert_iteratively(7)
    bst.insert_iteratively(8)
    bst.insert_iteratively(1)
    bst.insert_iteratively(6)

    print('----------------')
    print('Traversals')
    print('----------------')
    
    print(isBST_v2(bst.root))
    
