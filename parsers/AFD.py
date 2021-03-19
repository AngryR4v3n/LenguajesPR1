

from BuilderEnum import BuilderEnum
from BT import *
from TreeInfo import TreeInfo
from Transition import Transition
from Automata import Automata
import copy
from helper import *
class AFD:
    def __init__(self):
        self.fn = []
        self.initial = None
        self.final = None
        self.translator = None
        self.table = []
        self.finalDFA = []
        self.language = []
    
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
        self.final = st[0].first_pos
        st.reverse()
        self.initial = st[0].first_pos
        self.createDFA(tokens)
        self.translate()
        
        #print("STATES", self.fn)
        initial = self.fn[0]
        initial.set_initial(True)
        au = Automata([], self.language, initial, self.finalDFA, self.fn)
        print("automata", au)
        export_chart_subset(au)
        
        return au
        #print("done", table)

    def translate(self):
        vocab = vocabulary()
        diction = {}
        #iteramos para armar diccionario
        for trans in self.fn:
            if str(trans.get_start()) not in diction.keys():
                if trans.index:
                    diction[str(trans.get_start())] = vocab[trans.index]
        #iteramos otra vez para traducir
        for trans in self.fn:
            if trans.transition:
                trans.set_start(diction[str(trans.get_start())])
                trans.set_end(diction[str(trans.get_end())])

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
        translator = {}
        while counter < len(stackTree):
           
            if stackTree[counter].tree.number:
                #FIRST POS
                stackTree[counter].compute_first(treeObjs[counter])
                #LAST POS
                stackTree[counter].compute_last(treeObjs[counter])
                
                #translate
                if stackTree[counter].tree.root not in translator.keys():
                    translator[stackTree[counter].tree.root] = stackTree[counter].first_pos
                else:
                    translator[stackTree[counter].tree.root].extend(stackTree[counter].first_pos) 
                
            
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
        self.translator = translator
        #table = self.translate_table(table, stackTree)
        self.table = table

        
        return table


    def createDFA(self, tokens):
        language = []
        for token in tokens:
            if token.get_type() == "SYMBOL" and (token.get_value() != "#" or token.get_value() != "&"):
                if token.get_value() not in language:
                    language.append(token.get_value())
        self.language = language
        self.build_automata(language)
        return
    
   
    def build_automata(self, language, counter=0, checkArr=None):
        if checkArr == None:
            q0 = self.initial
            check = []
            dfa_states = []
            toState = Transition(start=q0, transition=None, end=q0)
            toState.set_initial(True)
            dfa_states.append(toState)
            #check.append(toState)

        elif len(checkArr) > 0:
            S = []
            check = checkArr
            dfa_states = copy.copy(checkArr)
            
        else:
            print("AFD", check)
            return "finished"
        print("States", dfa_states)
    
        for toState in dfa_states:
            if toState.get_mark():
                #toState = dfa_states.pop()
                continue
            toState.set_mark(True)
            #marcamos
            
            #obtenemos move de toState
            for letter in language:
                if letter != "&" and letter != "#":
                    #get traversal pasa a ser la union de los follow pos de cada uno de los elem
                    res = self.traverse(toState.get_end(), letter)
                    if len(res) > 0:
                        is_in_dfa = self.search_dfa_state(res, check)
                    
                        if not is_in_dfa:
                            #Creamos y pusheamos el estado al array y al dfa
                            toPush_arr = Transition(start=toState.get_end(), transition=letter, end=res)
                            toPush_arr.set_index(counter)
                            counter += 1 
                            if self.final[0] in toPush_arr.get_end():
                                toPush_arr.set_final(True)
                                self.finalDFA.append(toPush_arr)
                            self.fn.append(toPush_arr)
                            check.append(toPush_arr)

                            
                    
                        else:
                            createState = Transition(start=toState.get_end(), transition=letter, end=res)
                            createState.set_index(counter)
                            counter += 1 
                            if self.final[0] in createState.get_start():
                                createState.set_final(True)
                            
                            self.fn.append(createState)
                else:
                    continue
        
        is_over = self.is_over(check)
        
        if not is_over:
            self.build_automata(checkArr=check, language=language ,counter=counter)
        else:
            #print("TRANS",self.fn)
            return "finished"


    def traverse(self, state, letter):
        toReturn = []
        to_join_arr = self.translator[letter]
        
        for elem in to_join_arr:
            #obtenemos los follow pos
            for trans in self.table:
                if elem == trans.get_start():
                    #lo obtenemos
                    toReturn.extend(self.union(trans.get_end(),[elem]))
        
        return toReturn
    
    def union(self, arr1, arr2):

        res = []
        for elem in arr1:
            if elem not in arr2:
                res.append(elem)
        return res


    def search_dfa_state(self, state, stateRepo):
        for existing in stateRepo:
            if state == existing.get_end():
                return True
                break
        return False
            
    def is_over(self, dfa):
        counter = 0
        for state in dfa:
            if state.get_mark():
                counter += 1
        
        if counter == len(dfa):
            return True
        else:
            return False
