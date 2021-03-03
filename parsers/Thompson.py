

from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from State import *
from stack import Stack
from Automata import Automata
class Thompson:
    def __init__(self):
        #array of states
        self.stateCounter = 0
        self.opStack = Stack()    
        self.nfa = []
        self.automata = None
    
    def evalPostfix(self, tokens):
        self.automata = Automata([],[], None, {})
        """
        Definimos las reglas segun: 
        https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
        """
        
        for i in range(0, len(tokens)):
            
            currentToken = tokens[i]

            if currentToken.get_type() == "SYMBOL" and currentToken.get_value() != "&":
                #Regla #2: 
                
                state = State(self.stateCounter, {self.stateCounter + 1: [currentToken.get_value()]}, True, False)
                self.stateCounter += 1
                
                state2 = State(0, {}, False, True)
                self.stateCounter += 1
                
                
                
                au = Automata([], [], None, {})
                
                au.add_state(state)
                au.add_state(state2)
                
                self.opStack.add(au)
                
                

            #probablemente sea una operacion
            elif currentToken.get_type() != "SYMBOL":
                #regla #3: OR
                if currentToken.get_type() == "|":
                    
                    #sacamos del stack
                    nfa2 = self.opStack.pop()
                    

                    nfa1 = self.opStack.pop()

                    #armado de nfa base.
                    initialState = State(self.stateCounter, {}, True, False)
                    self.stateCounter += 1
                    initialState.set_neighbors(
                        {
                            nfa2.get_initial_state().get_id(): ["&"],
                            nfa1.get_initial_state().get_id(): ["&"]
                        }   
                    )
                    
                    finalState = State(self.stateCounter, {}, False, True)
                    self.stateCounter += 1

                    #Estado final de nfa 2 y nfa1 dejan de ser finales
                    final2 = nfa2.get_final_state() #devuelve estado que hacemos query
                    final2.set_neighbors({finalState.get_id(): ["&"]})
                    final1 = nfa1.get_final_state()
                    final1.set_neighbors({finalState.get_id(): ["&"]})

                    #Agregamos estados actualizados a los nfa viejos.
                    nfa2.add_state(final2)
                    nfa1.add_state(final1)

                    print(nfa2)
                    print(nfa1)
                    #nfa2.update_fn(final2.get_id())

                    
                    
                    
                    
                    
                    #nfa1.update_fn(final1.get_id())
                   
                
                    




                
                    
                




            """
            #Regla 1: Expresion & = epsilon
            if currentToken.get_type() == "SYMBOL" and currentToken.get_value() == "&":
                #creamos estado inicial.
                state = State({len(self.subNfa):{"neighbors": [len(self.subNfa)+1], "transition": "&"}}, False, False)
                state2 = State({len(self.subNfa):{"neighbors": [], "transition": ""}}, False, True)
                self.subNfa.append(state)
                self.subNfa.append(state2)
            #Regla 2: Expresion con simbolo 
            elif currentToken.get_type() == "SYMBOL" and currentToken.get_value() != "&":
                

            """

    

        
        
    def is_subset(self, arr1, arr2):
        for i in range(0, len(arr2)):
            for j in range(0, len(arr1)):
                if(arr2[i] == arr1[j]):
                    break

            if(j == len(arr1)):
                return False
                
        return True

    def thompson_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        self.evalPostfix(tokens)
        
    
        
        

                
