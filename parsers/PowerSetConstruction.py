from BuilderEnum import BuilderEnum
import sys  
import os
#import dentro de la carpeta parsers
sys.path.append(os.path.abspath(os.path.join("parsers")))
from Transition import *
from stack import Stack
from Automata import Automata

class PowerSet:
    def __init__(self):
        self.automata = []


    def build_automata(self):
        return "hey from powerSet!"
        