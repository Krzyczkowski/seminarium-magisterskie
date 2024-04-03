from graphs.DirectedGraph import DirectedGraph

g = DirectedGraph()
g.addEdge(0, 1)
g.addEdge(2,1)
g.addEdge(2,0)
g.bfs(2)
