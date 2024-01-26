import random

from main import get_states, add_new_states


# To improve the running time we use rules of "pruning"

# Rule 1: delete identical states
def pruning_rule1(states):
    for curr_state in states:
        for state in states:
            if curr_state.isEqual(state):
                states.remove(state)


def egalitarian_allocation_rule1(valuations: list[list[float]], initial_state):
    states = get_states(valuations, initial_state)
    pruning_rule1(states)
    max_min_value_state = max(states,
                              key=lambda state: min(state.valuation_of_player0, state.valuation_of_player1))
    return max_min_value_state


# Rule 2: delete every state where the optimistic bound is no better than the pessimistic bound
"""
Pessimistic bound: 
  the good result will not be worse - ex: divide the remaining objects randomlly 
Optimistic bound:
  the good result will not be better - ex: give the remaining objects to everyone  
"""
"""
State(state.number_of_objects + 1,
state.valuation_of_player0 + valuations[0][state.number_of_objects],
state.valuation_of_player1)
"""


def get_pessimistic_bound(state, total_objects, valuations):  # TODO
    remaining_objects = total_objects - state.number_of_objects
    random_choice = random.randint(0, 1)
    for object in remaining_objects:
        if random_choice == 0:
            state.valuation_of_player0 += valuations[0][object]
        else:
            state.valuation_of_player0 += valuations[1][object]
        state.number_of_objects = state.number_of_objects + 1
    pessimistic_bound = min(state.valuation_of_player0, state.valuation_of_player1)
    return pessimistic_bound



def get_optimistic_bound(state, remaining_objects):  # TODO
    pass


def pruning_rule2(states, total_objects, valuations):
    for state in states:
        pessimistic_bound = get_pessimistic_bound(state, total_objects, valuations)
        optimistic_bound = get_optimistic_bound(state, total_objects)
        if optimistic_bound <= pessimistic_bound:
            states.remove(state)
