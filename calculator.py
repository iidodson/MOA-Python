#~~~~ Standard calculator ~~~~#
#~~~~~ c. Indya Dodson ~~~~~~#

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

print("Here's the calculations")
print(f"{number1} + {number2} = {add(number1, number2)}")
print(f"{number1} - {number2} = {subtract(number1, number2)}")
print(f"{number1} * {number2} = {multiply(number1, number2)}")
print(f"{number1} / {number2} = {int(divide(number1, number2))}")
