import random
#                                                       Warning!
# This is my solution there are many ways to solve it and there is easiest way to solve this problem link down there
# https://replit.com/@appbrewery/rock-paper-scissors-end#main.py

random_integer = random.randint(0, 2)

selection = ["rock", "paper", "scissors"]
selection[0] = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

selection[1] = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

selection[2] = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(
    input("Choose one of them type 0 for rock,1 for paper,2 for scissors \n"))
# we have a shortcut to if user and computer choose the same thing we can do this
#   if user == random_integer:
#       print(f"{selection[user]}")
#       print(f"{selection[random_integer]}")
#       print("Play again!")
# If we do that we must delete or do something to the equal parts

if user == 0 and random_integer == 0:
    print(f"{selection[0]} ")
    print(f"{selection[0]} ")
    print("Play again!")
elif user == 0 and random_integer == 1:
    print(f"{selection[0]} ")
    print(f"{selection[1]} ")
    print("You lose!")
elif user == 0 and random_integer == 2:
    print(f"{selection[0]} ")
    print(f"{selection[2]} ")
    print("You win!")
elif user == 1 and random_integer == 0:
    print(f"{selection[1]} ")
    print(f"{selection[0]} ")
    print("You win!")
elif user == 1 and random_integer == 1:
    print(f"{selection[1]} ")
    print(f"{selection[1]} ")
    print("Play again!")
elif user == 1 and random_integer == 2:
    print(f"{selection[1]} ")
    print(f"{selection[2]} ")
    print("You lose!")
elif user == 2 and random_integer == 0:
    print(f"{selection[2]} ")
    print(f"{selection[0]} ")
    print("You lose!")
elif user == 2 and random_integer == 1:
    print(f"{selection[2]} ")
    print(f"{selection[1]} ")
    print("You win!")
elif user == 2 and random_integer == 2:
    print(f"{selection[2]} ")
    print(f"{selection[2]} ")
    print("Play again!")
