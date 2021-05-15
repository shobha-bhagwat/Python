from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        return self.graph[u].append(v)

    def DFS(self, graph, node, visited = set()):
        if node not in visited:
            print(node, " ", end="")
            visited.add(node)
            for neighbor in self.graph[node]:
                self.DFS(graph, neighbor, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal, starting from vertex 2")
g.DFS(g,2)
