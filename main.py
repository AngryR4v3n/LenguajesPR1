from Builder import *
from Parser import Parser
from postfix import Postfixer
#should return tokens

postfixer = Postfixer()



toBuild = "AFD"
automata = "(a|b)+"
if(toBuild == "AFD"):
    inFixRegEx = automata
    inFixRegEx += ".#"
    inFixRegEx = postfixer.fix_string(inFixRegEx)
    builder = Builder(inFixRegEx)
else:
    postfixRegex = postfixer.to_postfix(automata)
    builder = Builder(postfixRegex)



#paso de generar tokens
builder.generator()
#array de tokens devuelto por
tokens = builder.getTokenArr()
parser = Parser()

parser.parse(tokens, toBuild)