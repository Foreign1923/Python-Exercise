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
cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def give_card():
    cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and  len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    
    return sum(cards)


user_cards = []
computer_cards = []


for _ in range (2):
    
    user_cards.append(give_card)
    computer_cards.append(give_card)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer's first card:{computer_cards[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True