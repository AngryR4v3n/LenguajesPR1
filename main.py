from Builder import *
from Parser import Parser
from postfix import Postfixer
#should return tokens

postfixer = Postfixer()
postRegEx = postfixer.to_postfix("(01)*(10)*")

builder = Builder(postRegEx)


#paso de generar tokens
builder.generator()
#array de tokens devuelto por
tokens = builder.getTokenArr()
parser = Parser()

parser.parse(tokens, "Thompson")