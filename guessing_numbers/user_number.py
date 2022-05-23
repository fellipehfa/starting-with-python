import random


def computer_guesses(x):
  low = 1
  high = x
  feedback = ''
  
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low # could also be high b/c low == high
    feedback = input(f'Is your number {guess}? (h)igher, (l)ower, (c)orrect: ').lower()
    if feedback == 'h':
      low = guess + 1
    elif feedback == 'l':
      high = guess - 1
      
  print(f'Yay!!! Your number is {guess}')

computer_guesses(10)
