from graphs.Graph import Graph

class DirectedGraph(Graph):
   def addEdge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = [(v, weight)]
        else:
            self.graph[u].append((v, weight))
        
        if v not in self.graph:
            self.graph[v] = [(u, weight)]
        else:
            self.graph[v].append((u, weight))

    def print(self):
        for node in self.graph:
            print(f"{node} ->", ", ".join([f"{v}({w})" for v, w in self.graph[node]]))
