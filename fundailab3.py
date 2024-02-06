from aima.logic import expr
# Define constants for players, marks, and actions
X, O, BLANK = 'X', 'O', ' '

# Define symbols for the domain
Situation, Action, Square, Player, Mark = expr('Situation'), expr('Action'), expr('Square'), expr('Player'), expr('Mark')

# Define winning combinations (axioms for winning)
winning_combinations = [
    # Rows
    [(Square(1, 1), Mark(X)), (Square(1, 2), Mark(X)), (Square(1, 3), Mark(X))],
    [(Square(2, 1), Mark(X)), (Square(2, 2), Mark(X)), (Square(2, 3), Mark(X))],
    [(Square(3, 1), Mark(X)), (Square(3, 2), Mark(X)), (Square(3, 3), Mark(X))],

    # Columns
    [(Square(1, 1), Mark(X)), (Square(2, 1), Mark(X)), (Square(3, 1), Mark(X))],
    [(Square(1, 2), Mark(X)), (Square(2, 2), Mark(X)), (Square(3, 2), Mark(X))],
    [(Square(1, 3), Mark(X)), (Square(2, 3), Mark(X)), (Square(3, 3), Mark(X))],

    # Diagonals
    [(Square(1, 1), Mark(X)), (Square(2, 2), Mark(X)), (Square(3, 3), Mark(X))],
    [(Square(1, 3), Mark(X)), (Square(2, 2), Mark(X)), (Square(3, 1), Mark(X))]
]

# Define axioms for winning
def is_winning(situation, player):
    for combination in winning_combinations:
        if all((expr_in_situation(situation, square, mark) and mark == Mark(player)) for square, mark in combination):
            return True
    return False

# Define axioms for forced win (or draw)
def can_force_win(situation, player):
    # Define axioms for forced win here
    pass

# Define function to check if a given square and mark are in a situation
def expr_in_situation(situation, square, mark):
    return expr('In')(square, situation) & expr('Mark')(square, mark)

# Example usage
current_situation = Situation()
current_situation.append(expr('In')(Square(1, 1), Mark(X)))
current_situation.append(expr('In')(Square(1, 2), Mark(O)))
current_situation.append(expr('In')(Square(2, 2), Mark(X)))

print(is_winning(current_situation, X))
print(is_winning(current_situation, O))
