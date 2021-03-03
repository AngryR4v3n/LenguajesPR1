class State:
    """
    neighbors: should be an array of dictionaries
        {"1": ["B"], "2": ["A", "B"]}
    
    initial: boolean

    final: boolean
    """
    def __init__(self, uid, neighbors, initial, final):
        self.id = uid
        self.neighbors = neighbors
        self.isFinal = final
        self.isInitial = initial

    def get_neighbors(self):
        return self.neighbors

    def is_final(self):
        return self.isFinal
    
    def is_initial(self):
        return self.isInitial

    def get_id(self):
        return self.id

    def set_initial(self, val):
        self.isInitial = val

    def set_final(self, val):
        self.isFinal = val

    def set_neighbors(self, obj):
        self.neighbors = obj

    """
    Print for debugging 
    """
    def __repr__(self):
        return f"<State id: {self.id} with neighbors: {self.get_neighbors()}>"