'''
Imagine a literal stack of plates. If the stack gets too 
high, it might topple. Therefore, in real life we would 
likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that
mimics this. 

SetOfStacks should be composed of several stacks and should
create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave
identically to a single stack (that is, pop() should return
the same values as it would if there were just a single stack).

FOLLOW UP

Implement a function popAt(int index) which performs a pop 
operation on a specific sub-stack.
'''
from Stack import Stack

class SetOfStacks():
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []
        self.top_index = 0

        self.stacks.append(Stack())

    def push(self, value):
        top_stack = self.stacks[self.top_index]

        if top_stack.getSize() == self.threshold:
            self.stacks.append(Stack(value))
            self.top_index += 1
        else:
            top_stack.push(value)

    def pop(self):
        top_stack = self.stacks[self.top_index]
        if top_stack.isEmpty():
            print("All stacks are empty!")
            return None
        
        item = top_stack.pop()
        if top_stack.isEmpty() and self.top_index > 0:
            del(self.stacks[self.top_index])
            self.top_index -=1
        return item

    def peek(self):
        top_stack = self.stacks[self.top_index]
        return top_stack.peek()

    def isEmpty(self):
        return self.stacks[0].isEmpty() #if bottom stack is empty then all stacks are empty.

if __name__ == "__main__":
    sos = SetOfStacks(2)

    sos.push(1)
    sos.push(2)
    sos.push(1)

    sos.push(0)
    sos.push(0)
    sos.push(1)

    while (not sos.isEmpty()):
        print(sos.pop())