import queue


class Graph():
    def __init__(self, max_size):
        self.max_size = max_size
        self.nodes = [] * self.max_size

    def addNode(self, node):
        if len(self.nodes) < self.max_size:
            self.nodes.append(node)
        else:
            print("Limit reached. Graph is full.")

    def getNodes(self):
        return self.nodes


class Node():
    def __init__(self, name, *adjacent_nodes):
        self.name = name
        self.visited = False
        if adjacent_nodes:
            self.adjacent = adjacent_nodes
        else:
            self.adjacent = []

    def addAdjacent(self, n):
        self.adjacent.append(n)

    def getAdjacent(self):
        return self.adjacent

    def getName(self):
        return self.name

    def getVisited(self):
        return self.visited


def doesPathExistBFS(start, end):
    '''
    Using Breadth-First-Search:
    - Return True if a path exists from start to end node
    - Return False if not.
    '''
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        current = q.get()
        current.visited = True

        print(f"{current.getName()}")

        # check if end node reached
        if current == end:
            return True
        
        # add current's adjacent nodes to q 
        adj = current.getAdjacent()
        for a in adj:
            if not a.getVisited():
                q.put(a)
    
    return False
        

        


if __name__ == "__main__":
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")
    n5 = Node("e")
    n6 = Node("f")
    n7 = Node("g")
    n8 = Node("h")

    n1.addAdjacent(n2)

    n2.addAdjacent(n1)
    n2.addAdjacent(n3)
    n2.addAdjacent(n4)

    n3.addAdjacent(n2)

    n4.addAdjacent(n2)
    n4.addAdjacent(n5)

    n5.addAdjacent(n4)
    n5.addAdjacent(n6)
    n5.addAdjacent(n7)

    n6.addAdjacent(n5)

    n7.addAdjacent(n5)
    n7.addAdjacent(n8)

    n8.addAdjacent(n7)

    nodes = [n1, n2, n3, n4, n5, n6, n7, n8]

    result = doesPathExistBFS(n1, n8)

    if result:
        print("Path Exists!")
    else:
        print("No such path :(")

    '''
    for n in nodes:
        name = n.getName()
        for a in n.getAdjacent():
            print(f"Adjacent Node to {name}: {a.getName()}")
    '''

