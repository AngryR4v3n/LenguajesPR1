import sys  
import os
from BuilderEnum import BuilderEnum
sys.path.append(os.path.abspath(os.path.join("parsers")))
from stack import Stack
"""
Basado en https://www.free-online-calculator-use.com/infix-to-postfix-converter.html#
"""
class Postfixer:
    def __init__(self):
        self.stack = Stack()
        self.output = []
        self.enums = BuilderEnum
        self.precedence = {
            self.enums.KLEENE.value: 3,
            self.enums.PLUS.value: 2,
            self.enums.CONCAT.value: 1,
            self.enums.OR.value: 1,
        }
        self.checkOperands = 0
        self.operators = [
            self.enums.KLEENE.value, 
            self.enums.PLUS.value,
            self.enums.OR.value,
            self.enums.CONCAT.value
        ]
    
    
    def is_operand(self, ch):
        return ch.isalnum()

    def check_precedence(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.stack.peek()]
            return True if a <= b else False
        except KeyError:
            return False
    
    def fix_string(self, expr):
        fixed = ""
        for ch in expr:
            fixed += ch
            if self.is_operand(ch):
                self.checkOperands += 1
                if self.checkOperands <= 2:
                    pass
                else:
                    #si tenemos mas de dos letras pegadas, tenemos que meter un char de CONCAT
                    fixed += "."
                    self.checkOperands = 0
        return fixed

    def to_postfix(self, expr):
        expr = self.fix_string(expr)
        print("FIXED?",expr)
        for ch in expr:
            if self.is_operand(ch):
                self.output.append(ch)

            elif ch == self.enums.LEFT_PARENS.value:
                self.checkOperands = 0
                self.stack.add(ch)

            elif ch == ")":
                self.checkOperands = 0
                while ((not self.stack.is_empty()) and (self.stack.peek() != self.enums.LEFT_PARENS.value)):
                    a = self.stack.pop()
                    self.output.append(a)

                if (not self.stack.is_empty() and self.stack.peek() != self.enums.LEFT_PARENS.value):
                    print("ERR: Incorrect syntax")
                    exit(-1)
                else:
                    self.stack.pop()
            
            elif ch in self.operators:
                self.checkOperands = 0
                while(not self.stack.is_empty() and self.check_precedence(ch)):
                    
                    self.output.append(self.stack.pop())

                self.stack.add(ch)
            #non supported char
            else:
                
                print("ERR: Incorrect syntax")

                print("NON SUPPORTED CHAR")
                exit(-1)
                        
        while not self.stack.is_empty():
            self.output.append(self.stack.pop())
        
        return self.output
