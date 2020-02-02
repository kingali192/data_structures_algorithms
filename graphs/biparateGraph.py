class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = [[0 for column in range(V)] \ 
                                for row in range(V)]
        
        