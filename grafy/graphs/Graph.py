# GRAPH implementation with ADJESCENCY LIST
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    # add edge between u and v 
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
    def print(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print(f"{node} -> {neighbour}")

    def bfs(self, s):
        Q = deque([s])
        # set is more efficient than list for visited nodes 
        visited = set()
        visited.add(s)

        
        while Q:
            vertex = Q.popleft()
            print(vertex, end=" ")

            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    Q.append(neighbour)
                    visited.add(neighbour)
