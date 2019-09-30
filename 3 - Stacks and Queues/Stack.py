'''
Basic implementation of Stack ADT

Methods: push(), pop(), peek(), isEmpty()
'''

class stackNode():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self, data=None):
        self.top = stackNode(data)
        if data == None:
            self.size = 0
        else:
            self.size = 1
    
    def push(self, value):
        t = stackNode(value)
        if self.top == None:
            self.top = t
        elif self.top.data == None:
            self.top.data = value
        else:
            t.next = self.top
            self.top = t

        self.size += 1

    def pop(self):
        if self.top == None or self.top.data == None:
            return None
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def peek(self):
        if self.top == None or self.top.data == None:
            return None
        return self.top.data

    def isEmpty(self):
        return (self.top == None or self.top.data == None)
    
    def getSize(self):
        return self.size

