from BuilderEnum import BuilderEnum
class Postfixer:
    def __init__(self):
        self.array = []
        self.output = []
        self.enums = BuilderEnum
        self.precedence = {
            self.enums.KLEENE.value: 3,
            self.enums.PLUS.value: 2,
            self.enums.OR.value: 1,
        }
        self.checkOperands = 0
        self.operators = [
            self.enums.KLEENE.value, 
            self.enums.PLUS.value,
            self.enums.OR.value,
        ]
    
    def is_empty(self):
        if len(self.array) == 0:
            return True
        else:
            return False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.is_empty():
            return self.array.pop()
        else: 
            return "-1"

    def is_operand(self, ch):
        return ch.isalpha()

    def check_precedence(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
        except KeyError:
            return False

    def to_postfix(self, expr):
        for ch in expr:
            if self.is_operand(ch):
                #no deberiamos tener mas de dos letras pegadas
                self.checkOperands += 1
                if self.checkOperands <= 2:
                    self.output.append(ch)
                else: 
                    print("ERR: Incorrect syntax")
                    exit(-1)

            elif ch == self.enums.LEFT_PARENS.value:
                self.checkOperands = 0
                self.array.append(ch)

            elif ch == ")":
                self.checkOperands = 0
                while ((not self.is_empty()) and (self.peek() != self.enums.LEFT_PARENS.value)):
                    a = self.pop()
                    self.output.append(a)

                if (not self.is_empty() and self.peek() != self.enums.LEFT_PARENS.value):
                    print("ERR: Incorrect syntax")
                    exit(-1)
                else:
                    self.pop()
            
            elif ch in self.operators:
                self.checkOperands = 0
                while(not self.is_empty() and self.check_precedence(ch)):
                    
                    self.output.append(self.pop())

                self.array.append(ch)
            #non supported char
            else:
                print("ERR: Incorrect syntax")
                exit(-1)
        """                
        while not self.is_empty():
            self.output.append(self.pop())
        """
        return self.output
