from graphs.Graph import Graph

class DirectedGraph(Graph):
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

