# Here is the calculator in Python

number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))
operation = input("Enter the weather you want to solve\nAddition\nSubtraction\nMultiplication\nDivision\n")
if operation == 'Addition':
    sum = number1 + number2
    print("The sum of "+str(number1)+" and "+str(number2)+" is ",sum)
elif operation == 'Subtraction':
    sub = number1 - number2
    print("The subtraction of "+str(number1)+" and "+str(number2)+" is ",sub)
elif operation == 'Multiplication':
    Mul = number1 * number2
    print("The Multiplication of "+str(number1)+" and "+str(number2)+" is ",Mul)
elif operation == 'Division':
    if number2!=0:
        Div = number1 / number2
        print("The Division of "+str(number1)+" and "+str(number2)+" is ",Div)
    else:
        print("The Second Number Should not zero")
else:
    print("Invalid Input!")        

            
