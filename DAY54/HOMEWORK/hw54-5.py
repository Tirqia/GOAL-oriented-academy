# 1
number = int(input("enter your number:"))

if number % 2 == 0:
    print("It is even")
else:
    print("It is Odd")

# 2
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# 3
# Get a number from the user
number = int(input("Enter a number: "))

# Define a dictionary to store parity information
parity = {0: "even", 1: "odd"}

# Determine if the number is even or odd
result = parity[number % 2]

# Print the result
print(f"The number {number} is {result}.")
