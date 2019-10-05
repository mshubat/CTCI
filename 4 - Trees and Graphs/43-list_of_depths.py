'''
Given a binary tree, design an algorithm which creates a 
linked list of all the nodes at each depth (eg. if you 
have a tree with depth D, you'll have D linked lists).

Solution:

Could try a traversal of the tree, for each node that is 
visited for the first time append the node to the proper 
depth linked list. If the list does not yet exist, then
create it.

Do this untill all nodes in the tree have been traversed.
'''
from BST.binary_search_tree import binary_search_tree
from collections import defaultdict
from LinkedList import LinkedList

def lists_at_depths(node):
    list_at_depth = defaultdict(LinkedList)

    return (traverse_tree(node, list_at_depth))

def traverse_tree(node, list_at_depth, depth_above=-1):
    level = depth_above + 1

    list_at_depth[level].appendToTail(node.getValue())

    if node.getLeft():
        traverse_tree(node.getLeft(), list_at_depth, level)
    
    if node.getRight():
        traverse_tree(node.getRight(), list_at_depth, level)

    return list_at_depth


if __name__ == "__main__":
    # create the binary tree to be converted into lists
    tree = binary_search_tree(5)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)

    tree_as_lists = lists_at_depths(tree.root)

    for k,v in tree_as_lists.items():
        print(f"level: {k} values {v}")

    print("Test 2:")
    tree = binary_search_tree(8)
    tree.insert(6)
    tree.insert(2)
    tree.insert(0)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(14)
    tree.insert(256)

    tree_as_lists = lists_at_depths(tree.root)

    for k, v in tree_as_lists.items():
        print(f"level: {k} values {v}")
