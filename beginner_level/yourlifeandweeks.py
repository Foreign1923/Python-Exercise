# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)
age_day = (90 - age) * 365
age_week  = (90 - age) * 52
age_month = (90 - age) * 12

print("You have " + str(age_day) + " days, " + str(age_week) + " weeks, and " + str(age_month) + " months left.")
#message = print(f"You have  {age_day} days, {age_week} weeks, and {age_month} months left.") 