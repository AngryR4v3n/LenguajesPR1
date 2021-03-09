

from BuilderEnum import BuilderEnum

#import dentro de la carpeta parsers
from Transition import *
from stack import Stack
from Automata import Automata
from helper import * 
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
                print("DONE SYMB")
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
                        if(transition.get_transition() != None):
                            or_nfa.add_state(transition)
                    
                    #print(or_nfa)
                    print("DONE OR")
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
                    #estado inicial de nfa preexistente a nuevo estado de trans
                    initialState = Transition(self.stateCounter, "&",  initial)
                    initialEnd = Transition(initialState.get_start(), "&", final)
                    self.stateCounter += 1
                    
                    finalState = Transition(self.stateCounter, None, None)
                    #transicion de nfa final a final de nuevo nfa
                    finalTofinal = Transition(start=final, transition="&", end=finalState.get_start())
                    
                    self.stateCounter += 1
                    
                    
                    kleene_nfa = Automata([], [], initialState.get_start(), finalState.get_start(), [])
                    arr1 = nfa.arr_states()
                    unifiedArray = arr1
                    newTrans = [initialState,initialEnd, finalState, finalTofinal]
                    finalTrans = unifiedArray + newTrans
                    
                    for transition in finalTrans:
                        if(transition.get_transition() != None):
                            kleene_nfa.add_state(transition)

                    print("DONE KLEENE")
                    self.opStack.add(kleene_nfa)

                if currentToken.get_type() == "+":
                    nfa = self.opStack.pop()
                    
                    #encontramos estados finales e iniciales:
                    final = nfa.get_final_state()        
                    initial = nfa.get_initial_state()
                    #transicion de final a inicial del nfa preexistente
                    finalMod = Transition(start=final, transition="&", end=initial)

                    
                    nfa.add_state(finalMod)
                    #estado inicial de nfa preexistente a nuevo estado de trans
                    initialState = Transition(self.stateCounter, "&",  initial)
                    self.stateCounter += 1
                    
                    finalState = Transition(self.stateCounter, None, None)
                    #transicion de nfa final a final de nuevo nfa
                    finalTofinal = Transition(start=final, transition="&", end=finalState.get_start())
                    
                    self.stateCounter += 1
                    
                    
                    plus_nfa = Automata([], [], initialState.get_start(), finalState.get_start(), [])
                    arr1 = nfa.arr_states()
                    unifiedArray = arr1
                    newTrans = [initialState, finalState, finalTofinal]
                    finalTrans = unifiedArray + newTrans
                    
                    for transition in finalTrans:
                        if(transition.get_transition() != None):
                            plus_nfa.add_state(transition)

                    print("DONE PLUS")
                    self.opStack.add(plus_nfa)


                if currentToken.get_type() == ".":
                    nfa2 = self.opStack.pop()
                    nfa1 = self.opStack.pop()

                    initial = nfa2.get_initial_state()
                    final = nfa1.get_final_state()
                    #print("INIT", initial)
                    #print("FINAL", final)
                    for state in nfa2.arr_states():
                        #print("STATE", state)
                        if (state.get_start() == initial):
                            print("converting", state, "to ", final)
                            state.set_initial(final)

                    for state in nfa1.arr_states():
                        if(state.get_start() == final):
                            print("converting", state, "to ", final)
                            state.set_initial(initial)
                    merge_nfa = Automata([], [], nfa1.get_initial_state(), nfa2.get_final_state(), [])

                    opsNfa2 = nfa2.arr_states()
                    opsNfa1 = nfa1.arr_states()

                    merged = opsNfa2 + opsNfa1

                    for transition in merged:
                        if(transition.get_transition() != None):
                            merge_nfa.add_state(transition)

                    #print(merge_nfa)
                    print("DONE CONCAT")
                    self.opStack.add(merge_nfa)

        #opstack is ready to be exported
        return self.opStack



    def thompson_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        nfa = self.evalPostfix(tokens)
        #export a imagen
        export_chart(nfa.pop())
        
    
        
        

                
