"""
    Mini Task – Age Calculator

    Create a program that:

    Takes user's current age as input.
    Converts input into integer.
    Calculates age after 10 years.
    Displays both current age and future age.

    Example:

    Enter your age: 22

    Current Age: 22
    Age After 10 Years: 32
"""

age = int(input("Enter your age : "))
print("Current Age :",age)
age = age + 10
print("Age After 10 Years :",age)