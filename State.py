class State:
    def __init__(self, number_of_objects, valuation_of_player1, valuation_of_player2, left=None, right=None):
        self.number_of_objects = number_of_objects
        self.valuation_of_player1 = valuation_of_player1
        self.valuation_of_player2 = valuation_of_player2
        self.left = left
        self.right = right

    def isEqual(self, other):
        return (self.number_of_objects == other.number_of_objects) and (
                self.valuation_of_player1 == other.valuation_of_player1) and (
                self.valuation_of_player2 == other.valuation_of_player2)

    def __str__(self):
        return f"({self.number_of_objects}; {self.valuation_of_player1}, {self.valuation_of_player2})"

    def print_tree(self, depth=0):
        left_str = f"Left: {self.left}" if self.left else "Left: "
        right_str = f"Right: {self.right}" if self.right else "Right: "
        print(f"Root: {self}, {left_str}, {right_str}")
        if self.left:
            self.left.print_tree(depth + 1)
        if self.right:
            self.right.print_tree(depth + 1)

    def find_path(self, root, current_path=None):

        if current_path is None:
            current_path = []
        if root is None:
            return None

        current_path.append(root)
        if root.isEqual(self):
            return current_path.copy()

        left_path = self.find_path(root.left, current_path.copy())
        right_path = self.find_path(root.right, current_path.copy())

        return left_path or right_path
    def print_path(self, path):
        if path:
            print("Path to leaf:")
            for state in path:
                print(state)
        else:
            print("Target state not found in the tree.")

