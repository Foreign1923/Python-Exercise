import random
from time import sleep
from tkinter import N
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

number = random.randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
selection = input("Choose a difficulty. Type 'easy' or  'hard': ").lower()

state = int(0)
current_level = ["easy", "hard"]
current_level[0] = 10
current_level[1] = 5
if selection == "easy":
    print("You have 10 attempts ramining to guess the number.")
elif selection == "hard":
    print("You have 5 attempts remaining to guess the number.")
print(f"psst the number is: {number}")
    
if selection == "easy":   
    while  state < current_level[0]:
        state += 1
        
        attempt = int(input("Make a guess: "))
        if number > attempt:
            print("Too low.")
        elif number < attempt:
            print("Too high")
        elif number == attempt:
            print(f"You got it! The answer was {number}")
        reamining_Attempts = current_level[0] - state
        print(f"You have {reamining_Attempts} attempts reamining to guess the number.")

elif selection == "hard":
    while state < current_level[1]:
        state += 1
        attempt = int(input("Make a guess: "))
        if number > attempt:
            print("Too low")
        elif number < attempt:
            print("Too high")
        elif number == attempt:
            print(f"You got it! The answer was{number}")
        
        reamining_Attempts = current_level[1] - state
        print(f"You have {reamining_Attempts} attempts reamining to guess the number.")    
print("Out of attempts. Game over!")
'''
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

 
 
'''         