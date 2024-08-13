num1 =1
count_odd=0
count_even=0
sum_of_even=0
sum_of_odd =0

while num1 != 0:
    num1 = int(input("Input an integer (0 terminates): "))
    if num1 > 0:
        if num1 % 2== 0:
            count_even +=1
            sum_of_even = sum_of_even + num1
        elif num1 % 2 == 1:
            count_odd +=1
            sum_of_odd = sum_of_odd + num1
    else:
        print("Invalid number please enter a positive number!")
#    print("Input an integer (0 terminates): ",num1)

print("sum of odds:",sum_of_odd)
print("sum of evens:",sum_of_even)
print("odd count:",count_odd)
print("even count:",count_even)
print("total positive int count:",count_even + count_odd)
