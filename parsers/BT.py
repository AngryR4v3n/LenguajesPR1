from stack import Stack
from BuilderEnum import BuilderEnum
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

    def __repr__(self):
        return f"<Tree Root: {self.root} right: {self.right} left:{self.left}"

#recibe los tokens
def generate_tree(tokensArr):
    
    output = []
    stackOp = Stack()
    counter = 0

    for token in tokensArr:
        #if its a symbol, we just add a tree with empty child
        if token.get_type() == "SYMBOL":
            tree = BTree()
            tree.root = token.get_value()
            tree.left = None
            tree.right = None
            tree.number = counter
            
            output.append(tree)
            
        elif token.get_type() == "(":
            #we add it to the stack op which will have track of all operations to be done
            stackOp.add(token.get_type())
        
        elif token.get_type() == ")":

            while stackOp.length() > 0 and stackOp.peek() != "(":
                #empty until finding the "(", meanwhile we create the necessary trees
                rightOp = output.pop()
                leftOp = output.pop()
                op = stackOp.pop()
                tree = BTree()
                tree.root = op
                tree.left = leftOp
                tree.right = rightOp
                
                output.append(tree)
            stackOp.pop()
        else:
            #needs only one operator, special case
            if token.get_type() == "*" or token.get_type() == "+":
                uniOp = output.pop()
                tree = BTree()
                tree.root = token.get_type()
                tree.left = uniOp
                tree.right = None
            
                output.append(tree)
            #any other kind of operation of two operators ..
            else:
                while stackOp.length() > 0 and stackOp.peek() != '(':
                    op = stackOp.pop()
                    rightOp = output.pop()
                    leftOp = output.pop()
                    tree = BTree()
                    tree.root = op
                    tree.left = leftOp
                    tree.right = rightOp
                    
                    output.append(tree)
                #if its a symbol, get value, if not, get the type (where the char is stored)
                if(token.get_type() != "SYMBOL"):
                    stackOp.add(token.get_type())

                elif(token.get_type() == "SYMBOL"):
                    stackOp.add(token.get_value())
        
        counter += 1
        
    #while theres sth in the stack..
    while stackOp.length() > 0:
        rightOp = output.pop()
        leftOp = output.pop()
        op = stackOp.pop()
        tree = BTree()
        tree.root = op
        tree.left = leftOp
        tree.right = rightOp
        
        output.append(tree)
        counter += 1
    

    return output[-1]