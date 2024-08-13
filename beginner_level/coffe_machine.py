from coffe_ing import MENU
from coffe_ing import coin
coffe_machine = {
    "coffe" : 100,
    "water" : 100,
    "milk" : 100, 
}
choice = input(str("What would you like to order /espresso /latte /cappucion "))
def increment(choice):  
    if choice == "espresso":
        coffe_machine[0] -= 10
        coffe_machine[1] -= 20
    elif choice == "latte":
        coffe_machine[0] -=10
        coffe_machine[1] -=20
        coffe_machine[2] -=20
    elif choice == "cappucino":
        coffe_machine[0] -=10
        coffe_machine[1] -=20
        coffe_machine[2] -=30
    
increment(choice)
for_loop_statement = True
while for_loop_statement ==True:
    choice = input(str("What would you like to order /espresso /latte /cappucion "))
    amount= input(int("Please enter your moner here!"))
    x= input("would you like to continue? please say yes or no").lower()
    if x == "yes":
        increment(choice)
    elif x == "no":
        for_loop_statement = False
    else:
        print("invalid")
def costs (amount):
    count_birlik = 0
    count_onluk = 0
    count_beşlik = 0
    count_yirmibeşlik = 0
    remain_of =True
    if amount == "espresso":
        amount = amount - 5*coin["birlik"] + 2 * coin["yirmibeşlik"]
        remain_of = amount
        #buraya bir daha bak
        while(remain_of!=0):    
            if amount % coin["yirmibeşlik"]:
                count_birlik += 1
        
            elif amount % coin["beşlik"]:
                count_beşlik += 1
        
            elif amount % coin["onluk"]:
                count_onluk += 1
        
            elif amount % coin["birlik"]:
                count_birlik += 1
        
            else:
                print("invalid")
