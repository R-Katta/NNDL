# Take two numbers input 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Check for dividing by zero before performing division
if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Print the results of arithmetic operations
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
