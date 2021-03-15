from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from Transition import *
from Automata import Automata
import copy

class PowerSet:
    def __init__(self, automata):
        
        self.states = automata.get_states()
        self.language = automata.get_language()
        self.q0 = automata.get_initial_state()
        self.final = automata.get_final_state()
        self.fn = automata.arr_states()
        self.newfn = []
        self.counter = 0
        
    def e_closure(self, states, res=[]):
        e_set = res
        for state in states:
            if state not in e_set:
                e_set.append(state)
        
        for transition in self.fn:
            for state in states:
                if transition.get_transition() == "&" and transition.get_start() == state:
                    e_set.append(transition.get_end())
                    self.e_closure([transition.get_end()],res=e_set)
        
        return e_set

    def move(self, state, transition):
        reachable_set = []
        for op in self.fn:
            if op.get_start() == state and op.get_transition() == transition:
                reachable_set.append(transition)

        return reachable_set

    
    def search_by_start(self, arrState):
        tobechanged = []
        for state in self.fn:
            for otherState in arrState:
                if otherState == state.get_start():
                    tobechanged.append(state)
        
        return tobechanged

    
    def mark_states(self, arrState, dismark):
        
        tobechanged = self.search_by_start(arrState)
        for state in tobechanged:
            state.set_mark(dismark)

        return arrState

    def traverse(self, state, letter):
        toReturn = []
        for i in state:
            for st in self.fn:
                if i == st.get_start() and st.get_transition() == letter:
                    toReturn.append(st.get_end())
                    break
        return toReturn
    
    def build_automata(self, checkArr=None, counter=0):
        #revisamos las transiciones epsilon del start
        if checkArr == None:
            q0 = self.q0
            S = self.e_closure([q0])
            check = []
            dfa_states = []
            toState = Transition(start=S, transition=None, end=S)
            dfa_states.append(toState)
            check.append(toState)

        elif len(checkArr) > 0:
            counter += 1
            S = []
            check = checkArr
            dfa_states = copy.copy(checkArr)
            

            #S = self.e_closure(, res=[])
        else:
            print("SUBSET AFD", self.newfn)
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
            for letter in self.language:
                if letter != "&":
                    res = self.get_traversal(toState.get_end(), letter)
                    if len(res) > 0:
                        closure = self.e_closure(res, res=[])
                        is_in_dfa = self.search_dfa_state(closure, check)
        
                    
                        if not is_in_dfa:
                            #Creamos y pusheamos el estado al array y al dfa
                            toPush_arr = Transition(start=toState.get_end(), transition=letter, end=closure)
                            
                            
                            self.newfn.append(toPush_arr)
                            check.append(toPush_arr)

                            
                    
                        else:
                            pass
                            createState = Transition(start=toState.get_end(), transition=letter, end=closure)
                            self.newfn.append(createState)
            
        
        is_over = self.is_over(check)
        
        if not is_over:
            self.build_automata(checkArr=check, counter=counter)
        else:
            #print("FINAL",check)
            print("FINAL STATES", self.newfn)
            return "sabiaz q jelo kiti significa ola demonio?"
        #print("returning ", answer)
        
            
    
    def is_over(self, dfa):
        counter = 0
        for state in dfa:
            if state.get_mark():
                counter += 1
        
        if counter == len(dfa):
            return True
        else:
            return False


    #returns start of state if found in the array of transitions
    def search_dfa_state(self, dfa, stateList):
        
        for existing in stateList:
            if dfa == existing.get_end():
                    return existing.get_end()
        return None

    def search_nfa_state(self, relations):
        answer = []
        for existing in self.fn:
            for nfa_st in relations:
                if existing.get_start() == relation:
                    answer.append(existing)
        return answer
    def get_traversal(self, arr, letter):
        answer = []
        subset = self.traverse(arr, letter)
        for final in subset:
            answer.append(final)
            #print("to", answer)   

        
        return answer




    
        
        
    
        
    
        