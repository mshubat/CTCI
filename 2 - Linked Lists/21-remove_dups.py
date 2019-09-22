'''
Write code to remove duplicates from an unsorted
linked list. 

How would you solve this problem if a temporary buffer
is not allowed?
'''
from LinkedList import Node, LinkedList
from collections import defaultdict

def remove_duplicates(head):
    counts = defaultdict(int)
    n, c = head, head
    counts[n.data] += 1

    while (c.next != None):
        c = c.next
        if counts[c.data] == 1:
            # End of list reached looking for new data
            if c.next == None and n.next != None:
                n.next = None
        else:
            counts[c.data] += 1
            n.next = c
            n = c
    return head

if __name__ == "__main__":
    l = LinkedList(2)
    l.appendToTail(1)
    l.appendToTail(2)
    l.appendToTail(3)
    l.appendToTail(2)

    print(l)  # Before
    remove_duplicates(l.head)
    print(l)  # After

    l2 = LinkedList(1)
    l2.appendToTail(1)
    l2.appendToTail(4)
    l2.appendToTail(5)
    l2.appendToTail(3)
    l2.appendToTail(3)
    l2.appendToTail(2)

    print(l2)  # Before
    remove_duplicates(l2.head)
    print(l2)  # After
