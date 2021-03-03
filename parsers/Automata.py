class Automata:
    def __init__(self, states, language, start, fn):
        #array of state objs.
        self.states = states
        #Array of symbols
        self.language = language
        #start state obj of the automata
        self.start = start
        #fn is the array of objs
        # {
        # {"1": ["A"]}
        # }
        self.fn = fn

        #actual state (state obj)
        self.actualState = ""

    def get_states(self):
        return self.states

    def get_language(self):
        return self.language

    def get_initial_state(self):
        for st in self.states:
            if st.is_initial():
                return st


    def get_final_state(self):
        for st in self.states:
            if st.is_final():
                return st

    def remove_state(self, uid):
        i = 0
        for st in self.states:
            if st.get_id() == uid:
                self.states.pop(i)
            i += 1


    def update_fn(self, uid):
        self.fn = []
        for st in self.states:
            if st.get_id() == uid:
                neigh = st.get_neighbors()
        for i in range(len(neigh)):
            self.fn.append(neigh[i])
        
    def add_state(self, state):
        #agregamos transiciones.
        self.states.append(state)
        state_neighbors = state.get_neighbors()
    
        #array de forma {ESTADO_CONECTADO: ["CONEXION"]}
        
        #obtenemos las keys del vecino
        keyStates = list(state_neighbors.keys())
        
        #obtenemos las keys del automata
        automataStates = list(self.fn.keys())
        
        #si ya tenemos datos ingresados;
        if len(automataStates) > 0:
            for key in keyStates:
                # revisamos si no existe una regla
                # si no existe, agregamos dentro de un array la transicion
                
                
                if key not in automataStates:
                    self.fn[key] = state_neighbors[key]
                # si existe, extendemos el array existente al nuevo valor
                
                else:
                
                    self.fn[key].extend(state_neighbors[key])
                            
                
        else:   
            for key in keyStates:
                self.fn[key] = state_neighbors[key]



        
        #->loop a los simbolos introducidos por el nuevo estado
        # si no existe, le hacemos extend al array.
        for key in keyStates:     
            if state_neighbors[key] not in self.language:
                self.language.extend(state_neighbors[key])
        
                
        

    def __repr__(self):
        return f"<Automata fn: {self.fn} with language: {self.language}>"
        
        

            