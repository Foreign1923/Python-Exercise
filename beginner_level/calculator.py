
def multiply(n1, n2):
    return n1 * n2
def addition(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1- n2
def divide(n1, n2):
    return n1 / n2

operation = {
    "+": addition,
    "*": multiply,
    "-": substract,
    "/": divide
}
num1 = int(input("What is the first number?: "))
num2 = int(input("What is the second number?: "))

for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from line above: ")
calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")