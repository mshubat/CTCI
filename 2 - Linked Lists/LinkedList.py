class Node():
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList():
    def __init__(self, d):
        self.head = Node(d)

    def __str__(self):
        n = self.head
        s = str(n.data)
        while n.next != None:
            s += ", " + str(n.next.data)
            n = n.next
        return s

    def appendToTail(self, d):
        end = Node(d)  # Node to be added
        current = self.head
        while (current.next != None):
            current = current.next
        current.next = end

    def deleteNode(self, d):
        current = self.head
        if current.data == d:
            self.head = current.next
            return self.head
        
        while current.next != None:
            if current.next.data == d:
                current.next = current.next.next
                return self.head
            current = current.next

        print("Node Not Found.")
        return self.head


if __name__ == "__main__":
    linked = LinkedList(10)
    head = linked.head

    linked.appendToTail(5)
    linked.appendToTail(4)
    linked.appendToTail(3)
    linked.appendToTail(2)
    linked.appendToTail(1)
    linked.appendToTail(0)

    print(linked)
