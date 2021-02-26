from BuilderEnum import BuilderEnum
import copy
class AFD():
    def __init__(self):
        self.enums = BuilderEnum
        

    def afd_parser(self, tokens):
        print("Hi, im being passed this tokens! \n", tokens)
        if not self.isCorrect(tokens):
            print("Error: wrong input syntax!")
            exit(-1)
        else:
            print(":D allizwell")
        
    def isCorrect(self, tkk):
        #here we check if usage of parens is correct.
        left_count = 0
        right_count = 0
        for i in range(len(tkk)):
            #esto inicia si encontramos un left parens, deberiamos antes de chequear si hay mismo num
            #de ( y ).
            
            if tkk[i].get_type() == self.enums.LEFT_PARENS.value:
                left_count +=1
                arrTkk = copy.copy(tkk)
                counter = 0 
                #we pop first elem
                token = arrTkk.pop(0)
                
                while token.get_type() != self.enums.RIGHT_PARENS.value:
                    try:
                        token = arrTkk.pop(0)
                    except IndexError:
                        return False
                                
                    counter += 1
                #chequeamos si counter es mayor a 0, si pasa aqui es porque encontro un parens derecho
                #pero deberiamos chequear este caso ()
                if(counter<=0):
                    return False
            
            elif tkk[i].get_type() == self.enums.RIGHT_PARENS.value:
                right_count += 1
        
        if (right_count == left_count):
            return True
        else:
            return False
        
        

                
