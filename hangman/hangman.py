import random
import string

from hangman_visual import lives_visual_dict
from words import words

print("Welcome to Hangman!")

def get_valid_words(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
      word = random.choice(words)
    return word
  
def hangman():
  word = get_valid_words(words).upper()
  word_letters = set(word) # letters in the word
  alphabet = set(string.ascii_uppercase) # letters in the alphabet
  used_letters = set() # letters already used
  
  lives = 7
  
  while len(word_letters) > 0 and lives > 0:
    # letters used
    print('You have used:', ' '.join(used_letters))
    print('You have', lives, 'lives left.')
    
    # what current word looks like
    word_list = [letter if letter in used_letters else '_' for letter in word]
    print(lives_visual_dict[lives])
    print('Current word:', ' '.join(word_list))
  
    user_guess = input('Guess a letter: ').upper()
    if user_guess in alphabet - used_letters:
      used_letters.add(user_guess)
      if user_guess in word_letters:
        word_letters.remove(user_guess)
      else:
        lives = lives - 1
        print('Wrong!')
        
    elif user_guess in word_letters:
      print("You already guessed that letter!")
      
    else:
      print('Invalid character! Please try again.')

  if(lives == 0):
    print(lives_visual_dict[lives])
    print(f'You DIED! The word was {word}')
  else:
    print(f'You WIN! The word was {word}')

if __name__ == '__main__':
  hangman()

