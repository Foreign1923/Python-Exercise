from operator import index
import random

#allow the stages and create a variable logo and create this variable in module
#modify this corresponding to the final version
word = ["kedi", "kopek", "yılan", "papagan"]
random_word = random.choice(word)
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
lives = 6
print(f"{random_word}")
lst =[]
word_length = len(random_word)
for _ in range(len(random_word)): #or range(word_length)
    lst += "_"
print(lst)
guess = ""
game_over = False
while game_over == False:
    guess = input("Guess a word: ").lower()

    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            lst[position] = letter
    if guess not in random_word:
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
    
    print(f"{' '.join(lst)}")
    if "_" not in lst:
        game_over = True        
        print("you win")
        print(stages[lives])