from graphs.Graph import Graph

class UndirectedGraph(Graph):
    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        
        if v not in self.graph:
            self.graph[v] = [u]
        else:
            self.graph[v].append(u)
