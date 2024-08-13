from operator import truediv
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
card = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#card[10-11-12] = "K Q J"  
random_card1 = random.choice(card)
random_card2= random.choice(card)
type_of_card = ["♤", "♧", "♡", "♢"]
random_type_of_card1 = random.choice(type_of_card)
random_type_of_card2 = random.choice(type_of_card)

def usercards(shape_of1, shape_of2,num1, num2):
    if num1 == 11 or num2 == 11:
        if num1 == 11:
            print(f"[{shape_of1}][{shape_of2}{num2}]")
        elif num2 == 11:
            print(f"[{shape_of1}{num1}][{shape_of2}]")
        elif num1 == 11 and num2 == 11:
            print(f"[{shape_of1}][{shape_of2}]")
        else:
            print("Default")
    else:
        print(f"[{shape_of1}{num1}][{shape_of2}{num2}]")

    
    
random_card_pc1 = random.choice(card)
random_card_pc2 = random.choice(card)
random_type_of_card_pc1 = random.choice(type_of_card)
random_type_of_card_pc2 = random.choice(type_of_card)
yourcards = usercards(random_type_of_card1, random_type_of_card2, random_card1,random_card2)
# yourcards = [random_card1, random_card2]
print(logo)
print("Welcome to the BlackJack game!")
print('''Naturals. If a player's first two cards are an ace and a "ten-card" (a picture card or 10), 
giving a count of 21 in two cards, this is a natural or "blackjack."
If any player has a natural and the dealer does not, 
the dealer immediately pays that player one and a half times the amount of their bet. ''')

print(f"Your cards: {usercards(random_type_of_card1, random_type_of_card2, random_card1,random_card2)}")
print(f"Dealer: {usercards(random_type_of_card_pc1, random_type_of_card_pc2, random_card_pc1, random_card_pc2)}")
#should_condition = True
#while should_condition == True:
 #   print("What do you want to do?")
  #  print("Enter Hit me or not. Type 'y' for card or 'n' for stand")
