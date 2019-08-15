from node import node


class binary_search_tree:
    def __init__(self, value):
        self.root = node(True, value)
        self.count = 1

    def isroot(self, node):
        return node == self.root

    def insert_iteratively(self, value):
        '''
        Iterative approach: node insertion in BST
        '''
        new_node = node(False, value)

        current = self.root
        inserted = False

        while(not inserted):
            if value < current.getValue():
                next = current.getLeft()
                if next == None:
                    current.setLeft(new_node)
                    inserted = True
            elif value > current.getValue():
                next = current.getRight()
                if next == None:
                    current.setRight(new_node)
                    inserted = True
            else:
                print(f'Failure: {value} is already present in the tree.')
                return

            current = next
        print(f'Success: {value} has been inserted in the tree.')
        self.count += 1

    def insert_recursively(root, value):
        '''
        Recursive approach: node insertion in bst
        '''
        if root.getValue() == value:
            print(f'Failure: {value} is already present in the tree.')
            return
        elif value < root.getValue():
            if root.getLeft():
                binary_search_tree.insert_recursively(root.getLeft(), value)
            else:
                root.left = node(False, value)
        elif value > root.getValue():
            if root.getRight():
                binary_search_tree.insert_recursively(root.getRight(), value)
            else:
                root.right = node(False, value)

    @staticmethod
    def inOrder(node):
        '''
        Traverse the tree in order, print out the value
        at each node.
        '''

        if node.getLeft():
            binary_search_tree.inOrder(node.getLeft())
        print(node.getValue())
        if node.getRight():
            binary_search_tree.inOrder(node.getRight())

    def preOrder(node):
        '''
        Traverse the tree by first visiting the given node
        followed by its left, then right subtrees.
        '''
        print(node.getValue())

        if node.getLeft():
            binary_search_tree.preOrder(node.getLeft())
        if node.getRight():
            binary_search_tree.preOrder(node.getRight())

    def postOrder(node):
        '''
        Traverse the tree by traversing the nodes left
        subtree, then right, then visit the node.
        '''

        if node.getLeft():
            binary_search_tree.postOrder(node.getLeft())
        if node.getRight():
            binary_search_tree.postOrder(node.getRight())

        print(node.getValue())


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
    print("inOrder()")
    binary_search_tree.inOrder(bst.root)
    print("preOrder()")
    binary_search_tree.preOrder(bst.root)
    print("postOrder()")
    binary_search_tree.postOrder(bst.root)

    print('Create Tree with Recursive method')
    bst2 = binary_search_tree(5)
    binary_search_tree.insert_recursively(bst2.root, 3)
    binary_search_tree.insert_recursively(bst2.root, 7)
    binary_search_tree.insert_recursively(bst2.root, 7)
    binary_search_tree.insert_recursively(bst2.root, 8)
    binary_search_tree.insert_recursively(bst2.root, 1)
    binary_search_tree.insert_recursively(bst2.root, 6)
    print('----------------')
    print('Traversals')
    print('----------------')
    print("inOrder()")
    binary_search_tree.inOrder(bst2.root)
    print("preOrder()")
    binary_search_tree.preOrder(bst2.root)
    print("postOrder()")
    binary_search_tree.postOrder(bst2.root)
