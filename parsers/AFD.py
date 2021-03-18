

from BuilderEnum import BuilderEnum
from BT import *
from TreeInfo import TreeInfo
from Transition import Transition
from Automata import Automata
class AFD:
    def __init__(self):
        self.fn = {}
    def tree_to_stack(self, tree, res=[]):
        
        if tree:
            res.append(tree)
        if tree.left:
            self.tree_to_stack(tree.left, res=res)
        if tree.right:
            self.tree_to_stack(tree.right, res=res)
        
            
      
        return res

    def afd_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)

        tree = generate_tree(tokens)
        st = self.tree_to_stack(tree, [])
        
        st.reverse()
        treeInfo = self.generate_tree_info(st)
        table = self.compute_positions(treeInfo, st)
        #we turn it around to have depth first..
        st.reverse()
        initial = st[0]
        #self.createDFA(table, initial, final, tokens)
        print("done", table)

        
    def generate_tree_info(self, stackTree):
        treeInf = []
        for tree in stackTree:
            unit = TreeInfo(tree)
            treeInf.append(unit)

        return treeInf

    def compute_positions(self, stackTree, treeObjs):
        counter = 0
        #preparamos tabla
        table = []
        for tree in stackTree:
            if tree.tree.number:
                table.append(Transition(start=tree.tree.number, transition=None, end=[]))
        #primero todos los finales
        
        while counter < len(stackTree):
            #FIRST POS
            if stackTree[counter].tree.number:
                stackTree[counter].compute_first(treeObjs[counter])
                #LAST POS
                stackTree[counter].compute_last(treeObjs[counter])
            
            
            counter += 1
        

        #ahora las ops 
        counter = 0
        while counter < len(stackTree):
            #FIRST POS
            if not stackTree[counter].tree.number:
                stackTree[counter].compute_first(treeObjs[counter])
                #LAST POS
                stackTree[counter].compute_last(treeObjs[counter])
                stackTree[counter].compute_followpos(treeObjs[counter], table)
            
            counter += 1

        print("table", table)
        self.fn = table
        return table

    def createDFA(self, table, initial, tokens):
        language = []
        for token in tokens:
            if token.get_type() == "SYMBOL" and (token.get_value() != "#" or token.get_value() != "&"):
                if token.get_value() not in language:
                    language.append(token.get_value())
        au = Automata([],language,initial,None,[])
        state = Transition(start=initial,transition=None,end=None)
        state.set_initial(True)
        state.set_final(True)
        
    
    def traverse(self, state, letter):
        toReturn = []
        for i in state:
            for st in self.fn:
                if i == st.get_start() and st.get_transition() == letter:
                    toReturn.append(st.get_end())
                    break
        return toReturn

    def get_traversal(self, arr, letter):
        answer = []
        subset = self.traverse(arr, letter)
        for final in subset:
            answer.append(final)
            #print("to", answer)   

        
        return answer

    def build_automata(self, initial, language, counter=0, checkArr=None):
        if checkArr == None:
            q0 = initial
            check = []
            dfa_states = []
            toState = Transition(start=q0, transition=None, end=q0)
            toState.set_initial(True)
            dfa_states.append(toState)
            check.append(toState)

        elif len(checkArr) > 0:
            S = []
            check = checkArr
            dfa_states = copy.copy(checkArr)
            

            #S = self.e_closure(, res=[])
        else:
            print("AFD", check)
            return "finished"
        #marcamos
        #self.mark_states(S)
        
        answer = []
        print("States", dfa_states)
    
        for toState in dfa_states:
            if toState.get_mark():
                #toState = dfa_states.pop()
                continue
            toState.set_mark(True)
            #marcamos
            
            #obtenemos move de toState
            for letter in language:
                if letter != "&":
                    res = self.get_traversal(toState.get_end(), letter)
                    if len(res) > 0:
                        is_in_dfa = self.search_dfa_state(res, check)
        
                    
                        if not is_in_dfa:
                            #Creamos y pusheamos el estado al array y al dfa
                            toPush_arr = Transition(start=toState.get_end(), transition=letter, end=res)
                            toPush_arr.set_index(counter)
                            counter += 1 
                            if self.final in toPush_arr.get_start():
                                toPush_arr.set_final(True)
                            
                            self.newfn.append(toPush_arr)
                            check.append(toPush_arr)

                            
                    
                        else:
                            createState = Transition(start=toState.get_end(), transition=letter, end=closure)
                            createState.set_index(counter)
                            counter += 1 
                            if self.final in createState.get_start():
                                createState.set_final(True)
                            
                            self.newfn.append(createState)
            
        
        is_over = self.is_over(check)
        
        if not is_over:
            self.build_automata(checkArr=check, counter=counter)
        else:
            print("Oopsie")




        
    
        
        

                
