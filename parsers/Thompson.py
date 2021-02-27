

from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from State import State

class Thompson:
    
    
    def detect_pattern(self, tokens):
        """
        Definimos las reglas segun: 
        https://medium.com/swlh/visualizing-thompsons-construction-algorithm-for-nfas-step-by-step-f92ef378581b
        """
        #Regla 1: Expresion & = epsilon
        print("hola")
        

    def thompson_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
            
        
    
        
        

                
