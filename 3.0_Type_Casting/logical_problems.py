# Take your name as input and print it.
name = input("Enter your name : ")
print(name)

# Take age as input and convert to integer.
age = int(input("Enter your age : "))
print(age)

# Take height as input and convert to float.
height = float(input("Enter your height : "))
print(height)

# Take two numbers and print their types.
num1 = int(input("Enter first number : "))
print(num1,type(num1))
num2 = float(input("Enter second number : "))
print(num2,type(num2))

# Convert integer to string.
number = 34
print(number,type(number))
number = str(number)
print(number,type(number))

# Convert float to integer.
number = 34.3
print(number,type(number))
number = int(number)
print(number,type(number))

# Convert string "100" to integer.
number = "100"
print(number,type(number))
number = int(number)
print(number,type(number))

# Print three values using custom separator.
country = input("Enter your country : ")
state = input("Enter your state : ")
city = input("Enter your city : ")
print(country,state,city,sep='###')

# Print two messages on the same line.
country = input("Enter your country : ")
state = input("Enter your state : ")
print(country,end=' ')
print(state)

# Take name and city in a single input.
name,city = input("Enter name and city : ").split()
print(name,city)
