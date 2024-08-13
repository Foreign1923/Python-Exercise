import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids  = {}
def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${highest_bid}.")
print(logo)
print("Welcome to the secret auction program.")
selection = "yes"

while selection == "yes":
    name = input("What is your name?:")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    selection = input("Are there any other bidders? Type 'yes' or 'no':\n")
    if selection == "yes":
        
        os.system('cls')
    else:
        highest_bidder(bids)
