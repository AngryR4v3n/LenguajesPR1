class State:
    """
    neighbors: should be an array of dictionaries
        [{"neighbor": 1, "transition": "A"}, {"neighbor": 2, "transition": "B"}]
    
    initial: boolean

    final: boolean
    """
    def __init__(self, neighbors, initial, final):
    
        self.neighbors = neighbors
        self.isFinal = final
        self.isInitial = initial

    def get_neighbors(self):
        return self.neighbors

    def isFinal(self):
        return self.isFinal
    
    def isInitial(self):
        return self.isInitial