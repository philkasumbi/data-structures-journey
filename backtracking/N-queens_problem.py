def solve_n_queens(n):
    solutions = []
    board = []

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board.append(col)
                backtrack(row + 1)
                board.pop()

    backtrack(0)
    return solutions

# Example usage
n = 4
results = solve_n_queens(n)

def print_board(solution):
    for row in solution:
        line = ['.'] * n
        line[row] = 'Q'
        print(' '.join(line))
    print()

for sol in results:
    print_board(sol)
