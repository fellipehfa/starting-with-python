import random


def play():
  choices = ['R', 'P', 'S']
  user = input("(R)ock, (P)aper, (S)cissors? ").upper()
  computer = random.choice(choices)
  
  if user == computer:
    return f"It's a tie! I chose {computer}"
  
  # Rock beats scissors
  # Scissors beats paper
  # Paper beats rock
  if is_win(user, computer):
    return f'You beat me! I chose {computer}'
  
  return f'You lose! I chose {computer}'
  
def is_win(player, opponet):
  # return true if player wins
  # R > S
  if (player == 'R' and opponet == 'S') or \
    (player == 'S' and opponet == 'P') or \
    (player == 'P' and opponet == 'R'):
    return True

print(play())
print(play())
print(play())
print(play())
print(play())
