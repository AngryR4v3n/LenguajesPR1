class TreeInfo:
    def __init__(self, tree, nullable):
        self.tree = tree
        self.nullable = nullable
        self.first_pos = None
        self.last_pos = None
        self.forward_pos = None

    def compute_first(self):
        if(self.tree.root == "|"):
        
        elif(self.tree.root == "?"):
            return self.compute_first(self.tree.left) 
        elif(self.tree.root == "&"):
            return []

        else:

            #si es un simbolo..
            return self.tree

    def compute_last(self):

    def compute(self)
    