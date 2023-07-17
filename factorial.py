def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the factorial
fact = factorial(number)

# Display the result
print(f"The factorial of {number} is {fact}.")
