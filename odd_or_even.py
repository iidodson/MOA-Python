def odd_or_even(num1):
    if num1%2 == 0:
        print(f"{num1} is even")
    else:
        print(f"{num1} is odd")

num_input = int(input("Please enter your first number:"))

print(odd_or_even(num_input))
