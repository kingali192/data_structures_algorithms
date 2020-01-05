class Graph():
    def __init__(self):
        self.vertex = {}
    
    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))
            
    def addEdge(self, fromVertex, toVertex):
        if fromVertex in self.vertex:
            self.vertex[fromVertex].append(toVertex)
        else:
            self.vertex[fromVertex] = [toVertex]
            
    def BFS(self, startVertex):
        visited = [False]*len(self.vertex)
        queue = [] # list to store all vertices in BFS
        
        # mark node as visited and enqueue
        visited[startVertex] = True
        queue.append(startVertex)
        
        while queue:
            startVertex = queue.pop(0)
            #print(startVertex, end = ' ')
            for i in self.vertex[startVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
                    

        