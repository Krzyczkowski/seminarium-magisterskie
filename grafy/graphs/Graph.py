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
            n = Q.popleft()
            print(n, end=" ")

            for neighbour in self.graph.get(n,[]):
                if neighbour not in visited:
                    Q.append(neighbour)
                    visited.add(neighbour)


    def dfs(self,s):
        visited = set()
        visited.add(s)
        stack = []
        stack.append(s)
        print(s, end = ' ')
        while(len(stack)):
            n = stack[-1]
            stack.pop()

            if n not in visited:
                print(n, end=' ')
                visited.add(s)

            for neighbour in self.graph.get(n,[]):
                if neighbour not in visited:
                    stack.append(neighbour)
            
