import numpy as np
children = {'a':['b','c'],'b':['d','e'],'c':['f','g']} #mapping from state to child states
value = {'d':4,'e':3,'f':2,'g':1} # value of terminal states
action = {'d':'L','e':'R','f':'L','g':'R','b':'L','c':'R'} # mapping from state to the action that produces #that state



max_optimal_next_states = {}
min_optimal_next_states = {}

def produce_children(state):
    "Function to produce children of a state"
    return children.get(state,None)

def is_terminal(state):
    "Function to check if a state is terminal and return value of the state"
    if state in children:
        return False,0
    return True,value[state]

def get_action(next_state,current_state=None): 
    "Function to return action that moves player from current state to next state"
     #current state is redundant for this example as there is only one way to get to a state
    return action[next_state]

import random
def maximize(state):
    
    if state in max_optimal_next_states:
        return max_optimal_next_states[state]
    
    terminal_status,reward = is_terminal(state)
    if terminal_status:
        return state,reward # No further state so return same state
    
    max_state, max_score = None,-np.Inf
    max_states = []
    children = produce_children(state)
    for child in children:
        _,score = minimize(child)
        if score > max_score:
            max_state,max_score = child,score
            max_states = [max_state]
        elif score == max_score: 
            max_states.append(child)
            
    # If multiple actions are optimal, break ties randomly
    max_state = random.choice(max_states)
    max_optimal_next_states[state] = (max_state,max_score)
    
    return max_state,max_score

def minimize(state):
    
    if state in min_optimal_next_states:
        return min_optimal_next_states[state]
    
    terminal_status,reward = is_terminal(state)
    if terminal_status:
        return state,reward # No further state so return same state
    
    min_state, min_score = None,np.Inf
    min_states = []
    children = produce_children(state)
    for child in children:
        _,score = maximize(child)
        if score < min_score:
            min_state,min_score = child,score
            min_states = [min_state]
        elif score == min_score: 
            min_states.append(child)
    
    min_state = random.choice(min_states)
    min_optimal_next_states[state] =  (min_state,min_score)
    
    return min_state,min_score


def optimal_decision(state,player = 'Maximizer'):
    if player == 'Maximizer':
        max_state,_ = maximize(state)
        return get_action(max_state,state)
    else:
        min_state,_ = minimize(state)
        return get_action(min_state,state)
