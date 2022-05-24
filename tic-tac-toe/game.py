import math
import time

from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe:
  def __init__(self):
    self.board = self.make_board()
    self.current_winner = None # keep track of winner

  @staticmethod
  def make_board():
    return [' ' for _ in range(9)]

  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')

  @staticmethod
  def print_board_nums():
    number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in number_board:
      print('| ' + ' | '.join(row) + ' |')

  def make_move(self, square, letter):
    if self.board[square] == ' ':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False

  def winner(self, square, letter):
    row_ind = math.floor(square / 3)
    row = self.board[row_ind*3:(row_ind+1)*3]
    if all([s == letter for s in row]):
      return True

    col_ind = square % 3
    column = [self.board[col_ind+3*i] for i in range(3)]
    if all([s == letter for s in column]):
      return True

    if square % 2 == 0:
      diagonal1 = [self.board[i] for i in [0, 4, 8]]
      if all([spot == letter for spot in diagonal1]):
        return True

      diagonal2 = [self.board[i] for i in [2, 4, 6]]
      if all([spot == letter for spot in diagonal2]):
        return True

    return False

  def empty_squares(self):
    return ' ' in self.board

  def num_empty_squares(self):
    return self.board.count(' ')

  def avaible_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == ' ']

def play(game, x_player, o_player, print_game=True):
  if print_game:
    game.print_board_nums()

  letter = 'X' # X goes first
  while game.empty_squares():
    if letter == 'O':
      square = o_player.get_move(game)
    else:
      square = x_player.get_move(game)

    if game.make_move(square, letter):
      if print_game:
        print(letter + f'makes a move to square {square}')
        game.print_board()
        print('')

      if game.current_winner:
        if print_game:
          print(f"{letter} WINS!")
        return letter

      letter = 'O' if letter == 'X' else 'X'
    
    # if print_game:
    #   time.sleep(.8)

if __name__ == '__main__':
  # x_player = HumanPlayer('X')
  # o_player = RandomComputerPlayer('O')
  # o_player = HumanPlayer('O')
  i = 0
  scores = {'X': 0, 'O': 0, 'tie': 0}
  for _ in range(100):
    x_player = SmartComputerPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    result = play(t, x_player, o_player, print_game=True)
    if result == 'X':
      scores['X'] += 1
    elif result == 'O':
      scores['O'] += 1
    else:
      scores['tie'] += 1
    i += 1
  print(f"X wins {scores['X']} times \nO wins {scores['O']} times \ntie {scores['tie']} times")  
