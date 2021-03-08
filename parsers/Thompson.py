

from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from Transition import *
from stack import Stack
from Automata import Automata
class Thompson:
    def __init__(self):
        #array of states
        self.stateCounter = 0
        self.opStack = Stack()    
        self.nfa = []
    
    def evalPostfix(self, tokens):
        """
        Definimos las reglas segun: 
        https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
        """
        
        for i in range(0, len(tokens)):
            
            currentToken = tokens[i]
            
            if currentToken.get_type() == "SYMBOL" and currentToken.get_value() != "&":
                

                
                #Regla #2: 
                #0 -> {1: "B"}
                trans1 = Transition(start=self.stateCounter, transition=currentToken.get_value(), end=self.stateCounter+1)
                self.stateCounter += 1
                #1 -> {} y es final.
                trans2 = Transition(start=self.stateCounter, transition=None, end=None)
                self.stateCounter += 1
                
                #estados, alfabeto, estado inicial, estado final, funcion de transicion
                au = Automata([], [], trans1.get_start(), trans2.get_start(), [])
                au.add_state(trans1)
                au.add_state(trans2)
                #print(au)
                self.opStack.add(au)
                

            #sea una operacion
            elif currentToken.get_type() != "SYMBOL":

                #regla #3: OR
                if currentToken.get_type() == "|":
                    #sacamos del stack
                    nfa2 = self.opStack.pop()
                    
                    nfa1 = self.opStack.pop()

                    #armado de nfa base.
                    #TRANSICIONES
                    transitionInitial1 = Transition(start=self.stateCounter, transition="&", end=nfa1.get_initial_state())
                    transitionInitial2 = Transition(start=self.stateCounter, transition="&", end=nfa2.get_initial_state())
                    self.stateCounter += 1
                    transitionFinal1 = Transition(start=nfa1.get_final_state(), transition="&", end=self.stateCounter)
                    transitionFinal2 = Transition(start=nfa2.get_final_state(), transition="&", end=self.stateCounter)
                    self.stateCounter += 1

                    #Sacamos todas las transiciones del elem1 y elem2 
                    arr2 = nfa2.arr_states() #array
                    arr1 = nfa1.arr_states() #array
                    #unificamos los nfa
                    unifiedArray = arr2 + arr1
                    newTrans = [transitionInitial1, transitionInitial2, transitionFinal1, transitionFinal2]
                    finalTrans = unifiedArray + newTrans    
 
                    or_nfa = Automata([], [], transitionInitial1.get_start(), transitionFinal1.get_end(), [])
                    # me devuelve un array de States.
                    for transition in finalTrans:
                        if(transition.get_transition() != None and transition.get_end() != None):
                            or_nfa.add_state(transition)
                    
                    print(or_nfa)
                    self.opStack.add(or_nfa)
                
                #REGLA KLEENE
                if currentToken.get_type() == "*":
                    nfa = self.opStack.pop()
                    
                    #encontramos estados finales e iniciales:
                    final = nfa.get_final_state()        
                    initial = nfa.get_initial_state()
                    #transicion de final a inicial del nfa preexistente
                    finalMod = Transition(start=final, transition="&", end=initial)

                    
                    nfa.add_state(finalMod)

                    initialState = Transition(self.stateCounter, "&", initial)
                    
                    self.stateCounter += 1
                    
                    finalState = Transition(self.stateCounter, None, None)
                    initialEnd = Transition(self.stateCounter-1, "&", nfa.get_initial_state())
                    initialToFinal = Transition(start=initialState.get_start(), transition="&", end=finalState.get_start())       
                    #transicion de nfa final a final de nuevo nfa
                    finalTofinal = Transition(start=final, transition="&", end=finalState.get_start())
                    nfa.add_state(finalTofinal)
                    self.stateCounter += 1
                    
                    
                    kleene_nfa = Automata([], [], initial, final, [])
                    arr1 = nfa.arr_states()
                    unifiedArray = arr1
                    newTrans = [initialEnd, finalState, initialToFinal]
                    finalTrans = unifiedArray + newTrans
                    
                    for transition in finalTrans:
                        if(transition.get_transition() != None and transition.get_end() != None):
                            kleene_nfa.add_state(transition)

                    print(kleene_nfa)
                    self.opStack.add(kleene_nfa)




    def thompson_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        self.evalPostfix(tokens)
        
    
        
        

                
