from graphs.DirectedGraph import DirectedGraph

g = DirectedGraph()
g.addEdge(0, 1)
g.addEdge(1, 0)
g.addEdge(2,1)
g.bfs(1)
