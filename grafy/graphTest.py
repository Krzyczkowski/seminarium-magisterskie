from graphs.UndirectedGraph import UndirectedGraph
from graphs.DirectedGraph import DirectedGraph
print("BFS:")
g = UndirectedGraph()
g.addEdge(0, 1)
g.addEdge(2,1)
g.addEdge(2,0)
g.bfs(1)

print("\nDFS:")
g2 = DirectedGraph()
g2.addEdge(1,0)
g2.addEdge(0,2)
g2.addEdge(2,1)
g2.addEdge(0,3)
g2.addEdge(1,4)
g2.dfs(0)
