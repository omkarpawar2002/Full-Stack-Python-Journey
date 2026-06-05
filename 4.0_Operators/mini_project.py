"""
Simple Calculator

Build a calculator that:

Takes two numbers as input.
Performs:
Addition
Subtraction
Multiplication
Division
Floor Division
Modulus
Exponent
Displays all results clearly.

Example:

Enter First Number: 10
Enter Second Number: 3

Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333
Floor Division: 3
Modulus: 1
Exponent: 1000
"""

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
print("Addition:",num1 + num2)
print("Subtraction:",num1 - num2)
print("Multiplication:",num1 * num2)
print("Division:",num1 / num2)
print("Floor Division:",num1 // num2)
print("Modulus:",num1 % num2)
print("Exponent:",num1 ** num2)