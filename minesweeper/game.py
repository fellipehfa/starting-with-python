import random
import re


class Board:
    def __init__(self, size, number_bombs):
        self.size = size
        self.number_bombs = number_bombs
        
        self.board = self.make_new_board()
        self.assign_values_to_squares()
        
        self.dug = set()
    
    def make_new_board(self):
        board = [[None for _ in range(self.size)] for _ in range(self.size)]

        bombs_planted = 0
        while bombs_planted < self.number_bombs:
            location = random.randint(0, self.size**2 - 1)
            row = location // self.size
            column = location % self.size
            
            if board[row][column] == '*':
                # This square has already been planted.
                continue
            
            board[row][column] = '*' # plant the bombs
            bombs_planted += 1
        
        return board
    
    def assign_values_to_squares(self):
        for current_row in range(self.size):
            for current_column in range(self.size):
                if self.board[current_row][current_column] == '*':
                    continue
                
                self.board[current_row][current_column] = self.get_number_of_bombs_around(current_row, current_column)
    
    def get_number_of_bombs_around(self, row, column):
        # Let's iterate theough each of the 8 squares around the current square and count the number of bombs.
        # top left: (row - 1, column - 1)
        # top middle: (row - 1, column)
        # top right: (row - 1, column + 1)
        # left: (row, column - 1)
        # right: (row, column + 1)
        # bottom left: (row + 1, column - 1)
        # bottom middle: (row + 1, column)
        # bottom right: (row + 1, column + 1)
        
        number_of_bombs_around = 0
        for current_row in range(max(0, row-1), min(self.size-1, row+1)+1):
            for current_column in range(max(0, column-1), min(self.size-1, column+1)+1):
                if current_row == row and current_column == column:
                    continue
                if self.board[current_row][current_column] == '*':
                    number_of_bombs_around += 1
        return number_of_bombs_around
    
    def dig(self, row, column):
        self.dug.add((row, column))
        
        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True

        for current_row in range(max(0, row-1), min(self.size-1, row+1)+1):
            for current_column in range(max(0, column-1), min(self.size-1, column+1)+1):
                if (current_row, current_column) in self.dug:
                    continue # don't dig the same square twice
                self.dig(current_row, current_column)
        
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for column in range(self.size):
                if (row, column) in self.dug:
                    visible_board[row][column] = str(self.board[row][column])
                else:
                    visible_board[row][column] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key = len)))

        # print the csv strings
        indices = [i for i in range(self.size)]
        indices_row = '   '
        cells = []
        for idx, column in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (column))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, column in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (column))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
    
def play(size=10, number_bombs=10):
    board = Board(size, number_bombs)
    safe = True
    
    while len(board.dug) < board.size ** 2 - number_bombs:
        print(board)
        # with this regex we'll get the user's input even if user put spaces
        user_input = re.split(',(\\s)*', input("Where would you like to dig? (row, column): "))
        row, column = int(user_input[0]), int(user_input[-1])
        
        if row < 0 or row >= board.size or column < 0 or column >= board.size:
            print("Invalid location! Try again.")
            continue
        
        safe = board.dig(row, column)
        if not safe:
            break
        
    if safe:
        print("YOU WIN!!!")
    else:
        print("YOU DIED!!")
        
        board.dug = [(r, c) for r in range(board.size) for c in range(board.size)]
        print(board)
if __name__ == '__main__':
    play()
