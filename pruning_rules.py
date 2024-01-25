from main import get_states, add_new_states


# To improve the running time we use rules of "pruning"

# Rule 1: delete identical states
def pruning_rule1(states):
    for curr_state in states:
        for state in states:
            if curr_state.isEqual(state):
                states.remove(state)


def egalitarian_allocation_rule1(valuations: list[list[float]]):
    states = get_states(valuations)
    pruning_rule1(states)
    max_min_value_state = max(states,
                              key=lambda state: min(state.valuation_of_player1, state.valuation_of_player2))
    return max_min_value_state


# Rule 2: we will delete every state where the optimistic bound is no better than the pessimistic bound
"""
Pessimistic bound: 
  the good result will not be worse - ex: divide the reimagining objects randomlly 
Optimistic bound:
  the good result will not be better - ex: give the reimagining objects to everyone  
"""


def get_pessimistic_bound(state):  # TODO
    pass


def get_optimistic_bound(state):  # TODO
    pass


def pruning_rule2(states):
    for state in states:
        pessimistic_bound = get_pessimistic_bound(state)
        optimistic_bound = get_optimistic_bound(state)
        if optimistic_bound <= pessimistic_bound:
            states.remove(state)
