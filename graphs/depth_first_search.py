class Graph():
    def __init__(self):
        self.vertex = {}

    # for printing the Graph vertexes
    def printGraph(self):
        print(self.vertex)
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))

    # for adding the edge between two vertexes
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present,
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            # else make a new vertex
            self.vertex[fromVertex] = [toVertex]
    
    def DFS(self):
        visited = [False]*len(self.vertex)
        for i in range(len(self.vertex)):
            if visited[i] == False:
                self.DFSRec(i, visited)  
                
    def DFSRec(self, startVertex, visited):
        visited[startVertex] = True
        for i in self.vertex.keys():
            if visited[i] == False:
                self.DFSRec(i, visited)
             
    