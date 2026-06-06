# Check whether a number is positive.
num = int(input("Enter any number : "))
if(num > 0):
    print("Positive Number")

# Check whether a number is negative.
num = int(input("Enter any number : "))
if(num < 0):
    print("Negative Number")

# Check whether a person is eligible to vote.
age = int(input("Enter your age : "))
if(age >= 18):
    print("Eligible to vote")

# Check whether a student passed or failed.
marks = int(input("Enter your marks : "))
if(marks >= 35):
    print("pass")
else:
    print("fail")

# Compare two numbers and print the greater one.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 > num2):
    print(num1," is greater than ",num2)
else:
    print(num2," is greater than ",num1)

# Check whether a number is even or odd.
number = int(input("Enter any number : "))
if(number % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")

# Check whether age falls between 18 and 60.
age = int(input("Enter your age : "))
if(age >= 18 and age <= 60):
    print("Age falls in this range")
else:
    print("Age not falls in this range")

# Check whether a password matches a predefined password.
password = input("Enter any password : ")
if(password == "admin@123"):
    print("password is match")
else:
    print("password does not match")

# Check whether a number is divisible by 5.
number = int(input("Enter any number : "))
if(number % 5 == 0):
    print(number," is divisible by 5")
else:
    print(number," is not divisible by 5")

# Check whether a number is divisible by both 3 and 5.
number = int(input("Enter any number : "))
if(number % 5 == 0 and number % 3 == 0):
    print(number," is divisible by 5 and 3")
else:
    print(number," is not divisible by 5 and 3")

# Check whether a year is greater than 2000.
year = int(input("Enter any year : "))
if(year > 2000):
    print("year is greater than 2000")
else:
    print("year is not greater than 2000")

# Determine whether a person is a child or adult.
age = int(input("Enter your age : "))
if(age < 18):
    print("Child")
else:
    print("Adult")

# Check whether marks qualify for distinction.
marks = int(input("Enter your marks : "))
if(marks >= 75):
    print("Qualify for Distinction")
else:
    print("Not Qualify for Distinction")

# Determine the largest among two numbers.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
if(num1 > num2):
    print(num1," is greater than ",num2)
else:
    print(num2," is greater than ",num1)

# Determine the largest among three numbers.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if(num1 >= num2 and num1 >= num3):
    print(num1, "is the largest number")
elif(num2 >= num1 and num2 >= num3):
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")
    
# Check whether temperature indicates hot weather.
temperature = float(input("Enter temperature : "))
if(temperature > 30):
    print(temperature," is too hot")
else:
    print(temperature," is not too hot")

# Check whether salary is above a given limit.
salary = float(input("Enter your salary : "))
if(salary > 50000):
    print("Too Much Salary")
else:
    print("Enough Salary")

# Check whether a character is a vowel.
char = input("Enter any character : ")
if(char in "aeiouAEIOU"):
    print("It's a Vowel")
else:
    print("It's not a Vowel")

# Check whether a username is valid.
username = input("Enter your username : ")
if(username == "admin"):
    print("Valid Username!!")
else:
    print("InValid Username!!")

# Create a simple login verification condition.
username = input("Enter your username : ")
password = input("Enter your password : ")
if(username == "admin" and password == "admin@123"):
    print("Login Successful!!")
else:
    print("Login Failed!!")

# Take marks and assign grades using if elif else.
marks = int(input("Enter your marks : "))
if(marks >= 90):
    grade = "A"
elif(marks >= 70):
    grade = "B"
elif(marks >= 35):
    grade = "C"
else:
    grade = "F"
print("Student get",grade,"Grade")

# Check driving license eligibility using nested if.
age = int(input("Enter your age : "))
is_test_passed = True
if(age >= 18):
    if(is_test_passed):
        print("Eligible For Driving License")

# Use shorthand if to print "Positive" for positive numbers.
number = int(input("Enter number : "))
if(number > 0):print("Positive")

# Use a ternary operator to print "Even" or "Odd".
number = int(input("Enter number : "))
result = "Even" if(number % 2 == 0) else "Odd"
print(result)