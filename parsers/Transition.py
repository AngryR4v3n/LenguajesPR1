class Transition: 
    def __init__(self, start=None, transition=None, end=None):
        self.start = start
        self.transition = transition
        self.end = end

    def get_start(self):
        return self.start

    def get_transition(self):
        return self.transition
    
    def get_end(self):
        return self.end

    def __repr__(self):
        return f'<Transition from: {self.start} to {self.end} through {self.transition}>'
    



