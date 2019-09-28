'''
Basic implementation of Queue ADT

Methods: add(), remove(), peek(), isEmpty()
'''

class queueNode():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self, data):
        self.first = queueNode(data)
        self.last = self.first

    def add(self, data):
        t = queueNode(data)
        if self.first == None:
            self.first = t
            self.last = t
        else:
            self.last.next = t
            self.last = t

    def remove(self):
        if self.first == None:
            print("The Queue is Empty!")
            return None

        data = self.first.data
        self.first = self.first.next
        return data

    def peek(self):
        data = self.first.data
        return data

    def isEmpty(self):
        return self.first == None