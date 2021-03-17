

from BuilderEnum import BuilderEnum
from BT import *
from TreeInfo import TreeInfo
class AFD:
        
    def tree_to_stack(self, tree, res=[]):
        if len(res) == 0:
            stack = [];
        else:
            stack = res
        if tree != None:
            #si no es un hijo vacio, agregamos sus hijos no vacios
            if tree.left:
                stack.append(tree.left)
            if tree.right:
                stack.append(tree.right)
            self.tree_to_stack(tree.left, res=stack)
            
      
        return stack

    def afd_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)

        tree = generate_tree(tokens)
        st = self.tree_to_stack(tree, [])
        st.reverse()
        treeInfo = self.generate_tree_info(st)
        #we turn it around to have depth first..
        self.compute_positions(treeInfo, st)
        print("done", treeInfo)

    

        
    def generate_tree_info(self, stackTree):
        treeInf = []
        for tree in stackTree:
            unit = TreeInfo(tree)
            treeInf.append(unit)

        return treeInf

    def compute_positions(self, stackTree, treeObjs):
        counter = 0
        while counter < len(stackTree):
            print(stackTree[counter].compute_first(treeObjs[counter]))
            counter += 1
        #for tree in array:


        
    
        
        

                
