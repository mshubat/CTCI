'''
Implement a MyQueue class which implements a queue using
two stacks.

This implementation is faster when enques and dequeus are 
separated and batched. Each time the algorithm changes from
an enqueue to a dequeue it costs n operations. As items in
one stack are copied over to the other in order to maintain
the FIFO property.

Best Case: O(n)
Worst Case: O(n^2)
'''
from Stack import Stack

class MyQueue():
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def add(self, value):
        while (not self.s2.isEmpty()):
            self.s1.push(self.s2.pop())

        self.s1.push(value)

    def remove(self):
        while (not self.s1.isEmpty()):
            self.s2.push(self.s1.pop())

        return self.s2.pop()

    def peek(self):
        while (not self.s1.isEmpty()):
            self.s2.push(self.s1.pop())

        return self.s2.peek()

    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()


if __name__ == "__main__":
    q_of_s = MyQueue()

    q_of_s.add(10)
    q_of_s.add(8)
    q_of_s.add(5)
    q_of_s.add(3)
    q_of_s.add(1)

    q_of_s.remove()
    q_of_s.remove()

    q_of_s.add(99)

    print(q_of_s.peek())

    while (not q_of_s.isEmpty()):
        print(q_of_s.isEmpty())
        print(q_of_s.remove())

    print(q_of_s.isEmpty())

