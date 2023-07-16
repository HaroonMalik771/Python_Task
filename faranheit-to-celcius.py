def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Prompt the user to enter a temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the function
celsius = fahrenheit_to_celsius(fahrenheit)

# Display the result
print("The temperature in Celsius is:", celsius)
