# Conditional Statements :
'''
Conditional Statments are used to manipulate the flow of our program execution.

We know our code running from line number 1 to 10 line by line .
But we want our code from line number 4 to 8 will be executed only when specify condition is True that time we used conditional Statements.

There are 4 types of conditional statements in python :
    1.If statement
    2.If else statement
    3.If elif .... statement
    4.If elif .... else statement
'''

# If statement : 
'''
1.When we want to check only one condition then we used if statement.
2.The if block will be executed only when the condition specified after the if keyword is True otherwise if will be skipped.
'''
age = int(input("Enter your age : "))
if(age > 18):
    print("You can vote")


# If else statement :
'''
1.When we want to check 2 conditions either this or this then we used if-else statements.
2.The if block will be executed only when the condition specified after the if keyword is True otherwise if will be skipped and else block will get executed.
'''
age = int(input("Enter your age : "))
if(age > 18):
    print("You can vote")
else:
    print("You can not vote")


# If-elif statement :
'''
1.When we want to check more than 2 conditions then we used if-elif statement.
2.Here single if statement follow by multiple elif statements.
3.The if block will be executed only when the condition specified after the if keyword is True otherwise if will be skipped and check the next elif condition if this condition is match then elif block will be executed and if it false then elif will be skipped and check next conditions.......and if no condition match then it will skipped every condition and jump on next statement.
'''
color = input("Enter color name : ")
if(color == "black"):
    print("Black Color")
elif(color == 'white'):
    print("White Color")
elif(color == "blue"):
    print("Blue Color")


# If-elif-else statement :
'''
1.When we want to check more than 2 conditions then we used if-elif-else statement.
2.Here single if statement follow by multiple elif statements and multiple elif statements follow by single else statement.
3.The if block will be executed only when the condition specified after the if keyword is True otherwise if will be skipped and check the next elif condition if this condition is match then elif block will be executed and if it false then elif will be skipped and check next conditions.......and if no condition match then else block will be executed.
'''
color = input("Enter color name : ")
if(color == "black"):
    print("Black Color")
elif(color == 'white'):
    print("White Color")
elif(color == "blue"):
    print("Blue Color")
else:
    print("Color Mismatch")


# Nested if :
'''
When if inside another if is known as nested if statements
'''
age = int(input("Enter your age : "))
if(age > 18):
    if(age > 21):
        print("Eligible for Gate Exam")


# We can also put multiple conditions inside conditional statments by using logical operators : 
username = input("Enter your username : ")
password = input("Enter your password : ")
if(username == "admin" and password == "admin@123"):
    print("Login Successful!!")
else:
    print("Login Failed!!")


# shorthand if :
'''
When we have single statement in if block then we can write it on same line but if we have complex code then we write in normal way in multiple line.
'''
age = int(input("Enter your age : "))
if(age > 18):print("You can vote!")


# Ternary operator :
'''
1.Python does not use the ?: ternary operator syntax found in some other languages.
2.Instead, it provides a conditional expression:
value_if_true if condition else value_if_false
'''
marks = int(input("Enter your marks : "))
result = "Pass" if(marks >= 35) else "Fail"
print(result)