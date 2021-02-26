from Builder import *
from Parser import Parser
#should return tokens
builder = Builder("(a|b)")
#paso de generar tokens
builder.generator()
#array de tokens devuelto por
tokens = builder.getTokenArr()
parser = Parser()

parser.parse(tokens, "AFD")