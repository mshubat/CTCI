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