from graphviz import Digraph

def export_txt():
    print("hola")

"""
Example extracted from: https://graphviz.readthedocs.io/en/stable/examples.html#fsm-py
"""
def export_chart(nfa):
    f = Digraph('finite_state_machine', filename='nfa.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='reactangular')
    f.node(str(nfa.get_initial_state()))
    f.attr('node', shape='doublecircle')
    f.node(str(nfa.get_final_state()))

    f.attr('node', shape='circle')
    for transition in nfa.arr_states():
        f.edge(str(transition.get_start()), str(transition.get_end()), label=str(transition.get_transition()))
    
    f.view()

def export_chart_subset(dfa):
    f = Digraph('finite_state_machine', filename='dfa_subset.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr('node', shape='circle')
    for transition in dfa.arr_states():
        if transition.isInitial:
            f.attr('node', shape='reactangular')
        elif transition.isFinal:
            f.attr('node', shape='doublecircle')

        else:
            f.attr('node', shape='circle')             
        f.edge(str(transition.get_start()), str(transition.get_end()), label=str(transition.get_transition()))

    f.view()
    
