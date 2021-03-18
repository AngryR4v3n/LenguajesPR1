class Automata:
    def __init__(self, states, language, start, end, fn):
        #array of id states.
        self.states = states
        #Array of symbols
        self.language = language
        #start state obj of the automata
        self.start = start
        #end state
        self.end = end
        #fn is the array of transitions
        self.fn = fn
        #actual state (state obj)
        self.actualState = None


    def get_states(self):
        return self.states

    def get_language(self):
        return self.language
    
    def get_initial_state(self):
        return self.start

    def get_final_state(self):
        return self.end

    def set_initial_state(self, number):
        self.start = number

    def set_final_state(self, number):
        self.end = number

    def arr_states(self):
        return self.fn

    def add_state(self, trans):
        #extraemos los ids
        if trans.get_start() not in self.states:
            self.states.append(trans.get_start())

        if trans.get_end() not in self.states:
            self.states.append(trans.get_end())
        #agregamos a las funciones
        self.fn.append(trans)
        #agregamos a lenguaje
        if trans.get_transition() not in self.language and trans.get_transition() != None:
            self.language.append(trans.get_transition())

    def update_everything(self):
        for trans in self.fn:
            self.add_state(trans)

    
        
    def __repr__(self):
        return f"<Automata fn: {self.fn} with language: {self.language} states: {self.states}>\n STARTING: {self.start}, END: {self.end}"
        
        

            