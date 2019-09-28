'''
Basic implementation of Stack ADT

Methods: push(), pop(), peek(), isEmpty()
'''

class stackNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self, data):
        self.top = stackNode(data)
    
    def push(self, item):
        t = stackNode(item)
        if self.top == None:
            self.top = t
        else:
            t.next = self.top
            self.top = t

    def pop(self):
        if self.top == None:
            print("Stack is Empty!")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top == None:
            print("Stack is Empty!")
            return None
        return self.top.data

    def isEmpty(self):
        return self.top == None
