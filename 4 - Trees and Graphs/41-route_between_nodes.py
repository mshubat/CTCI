'''
Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.

'''

import queue
from Graphs.graph import Graph, Node

def doesPathExistBFS(start, end):
    q = queue.Queue()
    q.put(start)
    print(f"Searching for Path from {start.getName()} to {end.getName()}")

    while not q.empty():
        current = q.get()
        current.visited = True

        print(f"Node Visited: {current.getName()}")

        # check if end node reached
        if current == end:
            return True

        # add current's adjacent nodes to q
        adj = current.getAdjacent()
        for a in adj:
            if not a.getVisited():
                q.put(a)

    return False


def createFirstGraph():
    g = Graph(8)

    # create nodes
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")
    n5 = Node("e")
    n6 = Node("f")
    n7 = Node("g")
    n8 = Node("h")

    # Create connections
    # n1
    n1.addAdjacent(n2)
    # n2
    n2.addAdjacent(n1)
    n2.addAdjacent(n3)
    n2.addAdjacent(n4)
    # n3
    n3.addAdjacent(n2)
    # n4
    n4.addAdjacent(n2)
    n4.addAdjacent(n5)
    # n5
    n5.addAdjacent(n4)
    n5.addAdjacent(n6)
    n5.addAdjacent(n7)
    # n6
    n6.addAdjacent(n5)
    # n7
    n7.addAdjacent(n5)
    n7.addAdjacent(n8)
    # n8
    n8.addAdjacent(n7)

    nodes = [n1, n2, n3, n4, n5, n6, n7, n8]
    for n in nodes:
        g.addNode(n)

    return g

def create_second_graph():
    g = Graph(12)

    # create nodes
    n1 = Node("a")
    n2 = Node("b")
    n3 = Node("c")
    n4 = Node("d")
    n5 = Node("e")
    n6 = Node("f")
    n7 = Node("g")
    n8 = Node("h")
    n9 = Node("i")
    n10 = Node("j")
    n11 = Node("k")
    n12 = Node("l")

    # create connections
    n1.addAdjacent(n2)   #n1
    n2.addAdjacent(n3)   #n2
    n3.addAdjacent(n4)   #n3
    n3.addAdjacent(n5)
    n3.addAdjacent(n6)
    n4.addAdjacent(n7)   #n4
    n5.addAdjacent(n8)   #n5
    n6.addAdjacent(n9)   #n6
    n8.addAdjacent(n11)  #n8
    n9.addAdjacent(n10)  #n9
    n11.addAdjacent(n12) #n11

    # add nodes to graph
    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]
    for n in nodes:
        g.addNode(n)

    return g

if __name__ == "__main__":

    # Test 1
    # - - - - - - - - - - - - - - - - - -
    g = createFirstGraph()
    n3 = g.getNodes()[2]
    n6 = g.getNodes()[5]
    result = doesPathExistBFS(n3, n6)

    if result:
        print("Path Exists!")
    else:
        print("No such path :(")

    
    # Test 2
    # - - - - - - - - - - - - - - - - - -
    g = create_second_graph()
    n1 = g.getNodes()[0]
    n12 = g.getNodes()[11]
    
    print(n1.getName())
    print(n12.getName())
    
    result = doesPathExistBFS(n1, n12)

    if result:
        print("Path Exists!")
    else:
        print("No such path :(")
