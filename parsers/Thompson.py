

from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from State import State
from stack import Stack
class Thompson:
    def __init__(self):
        #array of states
        self.subNfa = []
        self.opStack = Stack()    
    
    def evalPostfix(self, tokens):
        """
        Definimos las reglas segun: 
        https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
        """
        
        for i in range(0, len(tokens)):
            
            currentToken = tokens[i]

            if currentToken.get_type() == "SYMBOL":
                self.opStack.add(currentToken)
            else: 
                #Evaluamos operador de dos operandos
                if self.opStack.length() >= 1:
                    tok1 = self.opStack.pop()
                    tok2 = self.opStack.pop()
                    self.pattern_detector(val1=tok1, val2=tok2, op=currentToken)
                #Operamos operador de un operando
                else:
                    tok1 = self.opStack.pop()
                    self.pattern_detector(val1=tok1, op=currentToken)
                    
                




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
                state = State({len(self.subNfa):{"neighbors": [len(self.subNfa)+1], "transition": currentToken.get_value()}}, False, False)
                state2 = State({len(self.subNfa):{"neighbors": [], "transition": ""}}, False, True)
                self.subNfa.append(state)
                self.subNfa.append(state2)

            """

    def pattern_detector(self, val1=None, val2=None, op=None):
        #deberiamos chequear si ambos val son symbols
        if val2:
            print("2 operand operator!")
        else:
            print("1 operand operator!")
        

    def thompson_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        self.evalPostfix(tokens)
        
    
        
        

                
