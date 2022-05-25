from pprint import pprint


def find_next_empty(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return row, column
    return None, None 

def is_valid(puzzle, guess, row, column):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    column_vals = []
    for index in range(9):
        column_vals.append(puzzle[index][column])
    column_vals = [puzzle[index][column] for index in range(9)]
    if guess in column_vals:
        return False
    
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3
    
    for current_row in range(row_start, row_start + 3):
        for current_column in range(column_start, column_start + 3):
            if puzzle[current_row][current_column] == guess:
                return False
    return True 

def sudoku_solver(puzzle):
    row, column = find_next_empty(puzzle)
    
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, column):
            puzzle[row][column] = guess
            
            if sudoku_solver(puzzle):
                return True

        puzzle[row][column] = -1
    
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(sudoku_solver(example_board))
    pprint(example_board)
