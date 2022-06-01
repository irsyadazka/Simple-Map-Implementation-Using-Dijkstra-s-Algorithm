import time

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.prevNode = {}
        self.distance = {}
        self.visited = {}
        self.timeGet = 0
        self.iteration = 0

    def readFile(self, path):
        lines = []
        filename = path + ".txt"
        with open(filename, 'r') as f:
            for line in f:
                src, dest, weight = line.split(' ')
                lines.append((src, dest, float(weight)))
        
        for node in lines:
            self.nodes.update([node[0], node[1]])

        self.edges = {node: set() for node in self.nodes}
        for edge in lines:
            self.edges[edge[0]].add((edge[1], edge[2]))

    def getMinimum(self, src):
        min = float("inf")
        min_node = src
        for node in self.nodes:
            if self.distance[node] < min and self.visited[node] == False:
                min = self.distance[node]
                min_node = node
        return min_node

    def printPath(self, dest):
        if self.prevNode[dest] == -1:
            print(dest, end=' ')
            return
        self.printPath(self.prevNode[dest])
        print("->", dest, end=' ')

    def printResult(self, src, dest):
        print("Shortest path from " + src + " to " + dest + ":")
        print("Distance: " + str(self.distance[dest]))
        self.printPath(dest)
        print("Time taken is", self.timeGet, "with", self.iteration, "iterations")

    def dijkstra(self, src, dest):
        self.iteration = 0
        self.distance[src] = 0

        for node in self.nodes:
            if node != src:
                self.distance[node] = float("inf")
            self.visited[node] = False
            self.prevNode[node] = -1

        start = time.time()
        for i in range(len(self.nodes) - 1):
            u = self.getMinimum(src)
            self.visited[u] = True

            if self.distance[u] == float("inf"):
                break

            for v in self.edges[u]:
                if self.visited[v[0]] == False and self.distance[u] + v[1] < self.distance[v[0]]:
                    self.distance[v[0]] = self.distance[u] + v[1]
                    self.prevNode[v[0]] = u
                self.iteration += 1

            if u == dest:
                break   
        end = time.time()
        self.timeGet = end - start

g = Graph()
g.readFile("case1")
g.dijkstra("a", "b")
g.printResult("a", "b")