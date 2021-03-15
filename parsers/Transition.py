class Transition: 
    def __init__(self, start=None, transition=None, end=None):
        self.start = start
        self.transition = transition
        self.end = end
        self.mark = False

    def get_start(self):
        return self.start

    def get_transition(self):
        return self.transition
    
    def get_end(self):
        return self.end

    def set_initial(self, number):
        self.start = number

    def set_end(self, number):
        self.end = number
    
    def get_mark(self):
        return self.mark
    
    def set_mark(self, data):
        self.mark = data

    def __repr__(self):
        return f'<Transition from: {self.start} to {self.end} through {self.transition}>'
    



