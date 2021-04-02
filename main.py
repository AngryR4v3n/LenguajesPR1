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
    opt = input("Type the number of the functionality you want to use: ")
    if opt != "6":
        
        if opt == "1":
            toBuild = "Thompson"
        elif opt == "2":
            toBuild = "PowerSet"
        elif opt == "3":
            toBuild = "AFD"
        
        if opt == "1" or opt == "2" or opt == "3":
            automata = input("Please type your RegEx: ") 
            res = generate(toBuild, automata, True)
            while res == -1:
                automata = input("Please type your RegEx: ") 
                res = generate(toBuild, automata, True)

        elif opt == "4":
            toBuild = "Thompson"
            automata = input("Type RegEx to simulate: ")
            res = generate(toBuild, automata, False)
            simulator(res, True)


        elif opt == "5":
            toBuild = "PowerSet"
            automata = input("Type RegEx to simulate: ")
            res = generate(toBuild, automata, False)
            simulator(res, False)
    else:
        print("bye!")
        exit(0)

#toBuild = "AFD"
#automata = "(a|b)*abb"

def generate(toBuild, automata, paint): 
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

    return parser.parse(tokens, toBuild, paint)

def simulator(automata, isNfa):
    string = input("Type the string to test: ")
    print("Simulating: \n", automata)
    if isNfa:
        ans = automata.simulate_NFA(string)
        if ans > 0:
            print("yes")
        else: 
            print("no")
    else:
        ans = automata.simulate_DFA(string)
        if ans > 0:
            print("yes")
        else:
            print("no")

#main()
def test():
    postfixer = Postfixer()
    postfixRegex = postfixer.to_postfix("(a|b)*abb")
    builder = Builder(postfixRegex)
    #paso de generar tokens
    builder.generator()
    #array de tokens devuelto por
    tokens = builder.getTokenArr()
    parser = Parser()
    parser.parse(tokens, "AFD", True)
test()