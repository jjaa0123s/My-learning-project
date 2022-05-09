import random
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  chance = 10
elif difficulty == "hard":
  chance = 5
else:
  print("Non sence.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

print(f"You have {chance} attempts remaining to guess the number.")

real_number = random.randint(1,100)

def make_guess():
  guess_number = int(input("Make a guess: "))
  if guess_number == real_number:
    print(f"You got it! The answer was {real_number}")
    return guess_number
  elif guess_number > real_number:
    print("Too high.")
    return guess_number
  elif guess_number < real_number:
    print("Too low.")
    return guess_number


while chance > 0:
  your_guess = make_guess()
  if real_number == your_guess:
    chance = 0
    break
  elif real_number != your_guess and chance > 1:
    print("Guess again.")
    chance -= 1
    print(f"You have {chance} attempts remaining to guess the number.")
  else:
    print("You have 0 attempts remaining to guess the number.")
    print("You lose.")
    break
