from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
            
    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    
    def DFShelp(self,u,v):
        visited[v] = True
        for i in self.graph[v]:
            if visited[v] == False:
                self.DFShelp(i, visited)
    
    def DFS(self, v):
        visited = [False] * len(self.graph)
        self.DFShelp(v, visited)
        
            
        
