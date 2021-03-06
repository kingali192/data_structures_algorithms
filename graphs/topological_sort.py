from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)
            
    def topologicalHelp(self, v, visited, stack):
        visited[v] == True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalHelp(i, visited, stack)
        stack.insert(0, v)
        
    def topological(self):
        visited = [False] * (self.V)
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalHelp(i, visited, stack)
        return stack
    
    

