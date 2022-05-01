#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

life = 6
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if life >= 0 and "_" in display:
    
    for position in range(word_length):
      letter = chosen_word[position]
      
      if letter == guess:
        display[position] = letter
    if guess not in display:
      print(stages[life])
      life -= 1

    
    print(f"{' '.join(display)}")
    


  elif "_" not in display:
    end_of_game = True
    print("You win.")
  else:
    end_of_game = True
    print("You lose.")




