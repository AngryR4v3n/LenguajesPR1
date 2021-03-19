from stack import Stack
from BuilderEnum import BuilderEnum
from TreeInfo import *
class BTree:
    def __init__(self):
        #Structure
        self.left = None
        self.right = None
        self.root = None
        
        #logic
        self.number = None
        self.nullable = None
        self.first_pos = None
        self.last_pos = None
        self.forward_pos = None
        
    def set_number(self, number):
        self.number = number



    def compute_followpos(self, table):
        if self.root == ".":
            left = self.left.last_pos
            right = self.right.first_pos
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
        elif self.root == "*":
            left = self.left.last_pos
            right = self.left.first_pos
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

        self.forward_pos = trans.get_end()
        return trans.get_end()

        """
        if self.left != None:
            compute_followpos(self.left, table)
        if self.right != None:
            compute_followpos(self.right, table)
        """

    def union( self, arr1, arr2):
        for elem in arr1:
            if elem not in arr2:
                arr2.append(elem)
        return arr2
    def __repr__(self):
        return f"<Tree Root: {self.root} right: {self.right} left:{self.left} \n first pos: {self.first_pos} last pos: {self.last_pos} follow pos {self.forward_pos}>"

def compute_positions(tree):
    print("compute tree", tree.root)
    """try:
        print("left values b4", tree.left.first_pos, tree.left.last_pos)
        print("right values b4", tree.right.first_pos, tree.right.last_pos)
    except:
        pass"""
    f = compute_first(tree)
    l= compute_last(tree)
    """try:
        print("left values after", tree.left.first_pos, tree.left.last_pos)
        print("right values after", tree.right.first_pos, tree.right.last_pos)
    except:
        pass"""
    #print("first", f, "last", l)
#recibe los tokens
def generate_tree(tokensArr):
    
    output = []
    stackOp = []
    counter = 0

    for token in tokensArr:
        #if its a symbol, we just add a tree with empty child
        if token.get_type() == "SYMBOL":
            tree = BTree()
            tree.root = token.get_value()
            tree.left = None
            tree.right = None
            tree.number = counter
            compute_positions(tree)
            stackOp.append(tree)
            counter += 1

        elif(token.get_type() != "SYMBOL"):
            if token.get_type() == "*":
                uniOp = stackOp.pop()
                tree = BTree()
                tree.root = token.get_type()
                tree.left = uniOp
                tree.right = None
                compute_positions(tree)
                stackOp.append(tree)
            

            #any other kind of operation of two operators ..
            
            else:
                op = token.get_type()
                rightOp = stackOp.pop()
                leftOp = stackOp.pop()
                tree = BTree()
                
                tree.root = op
                tree.left = leftOp
                tree.right = rightOp
                
                compute_positions(tree)

              
                stackOp.append(tree)
        
                
        
        
    

    return stackOp[-1]