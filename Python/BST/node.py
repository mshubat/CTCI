
class node:

    def __init__(self, isroot, value, left=None, right=None):
        self.root = isroot
        self.value = value
        self.left = left
        self.right = right

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right
    
    def getValue(self):
        return self.value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def isroot(self):
        return self.root