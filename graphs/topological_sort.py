class Graph():
    def __init__(self, count):
        self.vertex = {}
        self.count = count          # vertex count

    # for printing the Graph vertexes
    def printGraph(self):
        for i in self.vertex.keys():
            print(i,' -> ', ' -> '.join([str(j) for j in self.vertex[i]]))
            
    # adding the edge between two vertexes
    def addEdge(self, fromVertex, toVertex):
        if fromVertex in self.vertex.keys():
            self.vertex[fromVertex].append(toVertex)
        else:
            self.vertex[fromVertex] = [toVertex]
            self.vertex[toVertex] = []
            
    def topologicalSort(self):
        visited = [False]* self.count 
        stack = []
        for vertex in range(self.count):
            if visited[vertex] = False:
                self.topologicalSortRec(vertex, visited, stack)
        
        print(' '.join[str(i) for i in stack])
    
    def topologicalSortRec(self, vertex, visited, stack):
        pass
        # this is not done need this function for the topological sort.
            