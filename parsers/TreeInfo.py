class TreeInfo:
    def __init__(self, tree):
        self.tree = tree
        self.nullable = self.is_nullable(self.tree)
        self.first_pos = None
        self.last_pos = None
        self.forward_pos = None

    
    def compute_first(self, tree):
        if(tree.root == "|"):
            arr1 = tree.left.first_pos 
            arr2 = tree.right.first_pos
            unified = self.union(arr1, arr2)
            tree.first_pos = unified
            return unified

        elif(tree.root == "?" and (self.is_nullable(tree.left))):
            arr1 = tree.left.first_pos 
            arr2 = tree.right.first_pos
            unified = self.union(arr1, arr2)
            tree.first_pos = unified
            return unified
        elif(tree.root == "?" and not (self.is_nullable(tree.left))):
            arr1 = tree.left.first_pos 
            tree.first_pos = arr1
            return arr1

        elif(tree.root == "*"):
            arr1 = tree.left.first_pos 
            tree.first_pos = arr1
            return arr1
        
        elif(self.tree.root == "&"):
            return []

        else:
            #si es un simbolo..
            tree.first_pos = [tree.number]
            self.first_pos = [tree.number]
            return [tree.number]

    def compute_last(self, tree):
        if(tree.root == "|"):
            arr1 = tree.left.last_pos 
            arr2 = tree.right.last_pos
            unified = self.union(arr1, arr2)
            tree.last_pos = unified
            return unified

        elif(tree.root == "?" and (self.is_nullable(tree.right))):
            arr1 = tree.left.last_pos 
            arr2 = tree.right.last_pos
            unified = self.union(arr1, arr2)
            tree.last_pos = unified
            return unified
        elif(tree.root == "?" and not (self.is_nullable(tree.right))):
            arr1 = tree.right.last_pos 
            tree.last_pos = arr1
            return arr1

        elif(tree.root == "*"):
            arr1 = tree.left.last_pos 
            tree.last_pos = arr1
            return arr1
        
        elif(self.tree.root == "&"):
            return []

        else:
            #si es un simbolo..
            tree.last_pos = [tree.number]
            self.last_pos = [tree.number]
            return [tree.number]


    def compute_followpos(self, tree, table):
        if tree.root == "?":
            left = self.compute_last(tree.left)
            right = self.compute_first(tree.right)
            """
            for i in left:
                for num in right:
                    if num not in table[i]:
                        table[i].append(num)
            """
            for i in left:
                for trans in table:
                    if(trans.get_start() == i):
                        for num in right:
                            if num not in trans.get_end():
                                trans.get_end().append(num)
                    

                        break
        elif tree.root == "*":
            left = self.compute_last(tree)
            right = self.compute_first(tree)
            """
            for i in left:
                for num in right:
                    if num not in table[i]:
                        table[i].append(num)
            """
            for i in left:
                for trans in table:
                    if(trans.get_start() == i):
                        for num in right:
                            if num not in trans.get_end():
                                trans.get_end().append(num)
                        break
        elif tree.root == "+":
            left = self.compute_last(tree.left)
            right = self.compute_first(tree.left)
            for i in left:
                for trans in table:
                    if(trans.get_start() == i):
                        for num in right:
                            if num not in trans.get_end():
                                trans.get_end().append(num)
                        break
        if tree.left != None:
            self.compute_followpos(tree.left, table)
        if tree.right != None:
            self.compute_followpos(tree.right, table)


    def union(self, arr1, arr2):
        for elem in arr1:
            if elem not in arr2:
                arr2.append(elem)
        return arr2

    def is_nullable(self, node):
        if node:
            if node.root == "*":
                node.nullable = True
                return True
            elif node.root == "&":
                node.nullable = True
                return True
            elif node.root == "|":
                left = node.left.nullable
                right = node.right.nullable
                return left or right

            elif node.root == "?":
                left = node.left.nullable
                right = node.right.nullable
                return left and right

            #es un simbolo.
            else:
                node.nullable = False
                return False

    def __repr__(self):
        return f"<TreeInfo number is: {self.tree.number} first_pos: {self.first_pos} last_pos: {self.last_pos}>"


    #def compute(self):


    
    