from stack import Stack
class BTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.root = None

    def __repr__(self):
        return f"<Tree Root: {self.root} right: {self.right} left:{self.left}"

#recibe los tokens
def generate_tree(tokensArr):
    
    output = []
    stackOp = Stack()
    for token in tokensArr:
        
        if token.get_type() == "SYMBOL":
            tree = BTree()
            tree.root = token.get_value()
            output.append(tree)
            
        elif token.get_type() == "(":
            
            stackOp.add(token.get_type())
        
        elif token.get_type() == ")":

            while stackOp.length() > 0 and stackOp.peek() != "(":
                rightOp = output.pop()
                leftOp = output.pop()
                op = stackOp.pop()
                tree = BTree()
                tree.root = op
                tree.left = leftOp.root
                tree.right = rightOp.root
                output.append(tree)
            stackOp.pop()
        
        else:
            #needs only one operator, special case
            if token.get_type() == "*":
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
        if (len(output) == 1):
            return output[-1]

    return output[-1]