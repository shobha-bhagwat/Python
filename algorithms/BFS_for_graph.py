from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        return self.graph[u].append(v)


    def BFS(self, graph, vertex): # Breadth-first traversal

        queue = deque([vertex])
        level = {vertex: 0}
        parent = {vertex: None}
        i = 1
        while queue:
            v = queue.popleft()
            for neighbor in self.graph[v]:
                if neighbor not in level:
                    queue.append(neighbor)
                    level[neighbor] = i
                    parent[neighbor] = v
            i+=1
        return level, parent


    def simple_BFS(self, graph, vertex): # Breadth-first traversal

        queue = deque([vertex])
        visited = set()
        while queue:
            vertex = queue.popleft()
            print(vertex, " ", end="")
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)




g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal, starting from vertex 2")
print(g.BFS(g,2))
g.simple_BFS(g,2)
