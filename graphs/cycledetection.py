from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
    def isCycleHelp(self, v, visited, parent):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                if self.isCycleHelp(i, visited, v):
                    return True
            elif parent != i:
                return True
        return False
    
    def isCycle(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                if self.isCycleHelp(i, visited, -1) == True:
                    return True:
        return False
    
        
                