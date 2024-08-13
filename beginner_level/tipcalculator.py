#each person has 150$
print("Welcome to the tip calculator!")

bill =float(input("What aws the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or15?"))
split = int(input("How many people to split the bill?"))

pay = (bill / split) * 1.12
print(f"Each person should pay: ${round(pay,2)}")
