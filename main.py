"""
Search in the state space:
State is a vector with length n+1 such that: 
- The first element is the number of objects that was divided so far
- The rest n elements are the valuations of the players so far

The idea:
1. Initialize empty State: (0; 0,0)
2. For every object:
    For every exist State we will create more States by add one more object to the players
3. From all the last States , we choose the State with the max min value 

"""

from State import State
from StatesTree import StatesTree


def add_new_states(current_states):
    new_states = []
    for state in current_states:
        # For every new state - nether player1 gets the object or player2 gets the object
        new_state_for_player1 = State(state.number_of_objects + 1,
                                      state.valuation_of_player1 + valuations[0][state.number_of_objects],
                                      state.valuation_of_player2)
        new_state_for_player2 = State(state.number_of_objects + 1, state.valuation_of_player1,
                                      state.valuation_of_player2 + valuations[1][state.number_of_objects])

        state.left = new_state_for_player1
        state.right = new_state_for_player2
        new_states.extend([new_state_for_player1, new_state_for_player2])
    return new_states


def get_states(valuations: list[list[float]],initial_state):
    number_of_objects = len(valuations[0])

    print(f"Initial State: {initial_state.__str__()}")

    current_states = [initial_state]

    for i in range(number_of_objects):
        print(f"\nObject {i}: ")
        new_states = add_new_states(current_states)

        print("The new states: ")
        for i, state in enumerate(new_states):
            print(f"State {i}: {state.__str__()}, Sum is: {state.valuation_of_player1 + state.valuation_of_player2}")
        current_states = new_states
    print("The tree: \n")
    # initial_state.print_tree()

    return current_states


# TODO: change the output to be player i gets items ** with values **
def egalitarian_allocation(valuations: list[list[float]]):
    initial_state = State(0, 0, 0)
    states = get_states(valuations, initial_state)
    final_state = max(states,
                              key=lambda state: min(state.valuation_of_player1, state.valuation_of_player2))

    final_state.print_path(final_state.find_path(initial_state))
    return final_state


if __name__ == '__main__':
    # valuations = [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]]
    # valuations = [[4, 5, 6], [6, 5, 4]]
    valuations = [[11, 55], [33, 44]]
    # valuations = [[11, 55, 66], [33, 44, 22]]
    # valuations = [[11, 66], [44, 22]]
    # valuations = [[11, 22, 33, 44], [22, 11, 44, 33]]

    result_state = egalitarian_allocation(valuations)
    print(f"Egalitarian Allocation: {result_state}")


