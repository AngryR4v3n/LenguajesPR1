from Builder import *
from Parser import Parser
from postfix import Postfixer
#should return tokens

postfixer = Postfixer()



toBuild = "AFD"
if(toBuild == "AFD"):
    inFixRegEx = postfixer.fix_string("(a|b)*abc")
    inFixRegEx += "?#"
    builder = Builder(inFixRegEx)
else:
    postfixRegex = postfixer.to_postfix("(a|b)*abb")
    builder = Builder(postfixRegex)



#paso de generar tokens
builder.generator()
#array de tokens devuelto por
tokens = builder.getTokenArr()
parser = Parser()

parser.parse(tokens, toBuild)