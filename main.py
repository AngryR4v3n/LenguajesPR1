from Builder import *
from Parser import Parser
from postfix import Postfixer
#should return tokens



def main():
    print("NFA-DFA by Fran :(")

    print("NOTICE: & means epsilon, be cautious for this.")

    x = True
    print("1. Generate NFA (Thompson)")
    print("2. Generate DFA (PowerSet construction)")
    print("3. Generate DFA (direct method)")
    print("4. Simulate NFA")
    print("5. Simulate DFA")
    print("6. Exit")
    print("=========================================")
    print("=========================================")
    while x:
        opt = input("Choose one of the following functions:")

        if opt != "6":
            
            if opt == "1":
                toBuild = "Thompson"
            elif opt == "2":
                toBuild = "PowerSet"
            elif opt == "3":
                toBuild = "AFD"
            
            if opt == "1" or opt == "2" or opt == "3":
                automata = input("Please type your RegEx: ") 
                generate(toBuild, automata)
        else:
            print("bye!")
            exit(0)

#toBuild = "AFD"
#automata = "(a|b)*abb"

def generate(toBuild, automata): 
    postfixer = Postfixer()
    if(toBuild == "AFD"):
        inFixRegEx = "("+automata+")"
        inFixRegEx += ".#"
        inFixRegEx = postfixer.to_postfix(inFixRegEx)
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


main()