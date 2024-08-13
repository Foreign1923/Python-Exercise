import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_item = len(names)
random_person = random.randint(0, num_item-1)
who_gonna_pay = names[random_person]
print(f"{who_gonna_pay} is going to pay everbody's meal ")
