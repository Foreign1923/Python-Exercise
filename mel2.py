
Number = int(input("Please Enter the Range : "))



def Fibonaccı(n):

    # Initializing First and Second Values
    i = 0
    First_Value = 1
    Second_Value = 1

# Find & Displaying
    while (i < n):
        if (i <= 1):
            Next = i
        else:
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
        print(Next)
        i= i+1
    
ratio = 0.0
First_number = Fibonaccı(Number)
Second_Number = Number -1
Fibonaccı(Second_Number)
ratio = First_number / Second_Number
print(f"so this is the ratio: {ratio}")

count = 0
while ratio != ratio:
    count += 1

print(f"so this is the count: {count}")
