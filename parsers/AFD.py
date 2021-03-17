

from BuilderEnum import BuilderEnum
from BT import *
class AFD:
        
    def tree_to_stack(self, tree, res=[]):
        if len(res) == 0:
            stack = [];
        else:
            stack = res
        
        if isinstance(tree, str): 
            return stack

        stack.append(tree)
        
        self.tree_to_stack(tree.left, res=stack)
        
        return stack

    def afd_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        print("BUILDING BINARY TREE!")
        #tree = BT.BTree()
        tree = generate_tree(tokens)
        st = self.tree_to_stack(tree, [])
        print("done", st)

    def is_nullable(self, node):
        if node.root == "*":
            return True
        elif node.root == "&":
            return True
        elif node.root == "|":
            return self.is_nullable(node.left) or self.is_nullable(node.right)

        elif node.root == "?":
            return self.is_nullable(node.left) and self.is_nullable(node.right)
        else:
            return True

        
    #def first_pos(self, array):
        #for tree in array:


        
    
        
        

                
