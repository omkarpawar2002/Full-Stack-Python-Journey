# Take user name as input and print it.
name = input("Enter name : ")
print(name)

# Take age as input and convert to integer.
age = int(input("Enter age : "))
print(age)

# Take salary as input and convert to float.
salary = float(input("Enter salary : "))
print(salary)

# Convert integer 100 to string.
num = 200
num = str(num)
print(num,type(num))

# Convert float 50.5 to integer.
num = 50.5
num = int(num)
print(num,type(num))

# Convert string "500" to integer.
num = "500"
num = int(num)
print(num,type(num))

# Convert string "99.9" to float.
num = "99.9"
num = float(num)
print(num,type(num))

# Take two numbers from user and display them.
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
print(num1,num2)

# Print values using sep="-".
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
print(num1,num2,sep='-')

# Print values using sep=" | ".
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
print(num1,num2,sep=" | ")

# Use end=" " to print on same line.
num1 = int(input("Enter number : "))
num2 = int(input("Enter number : "))
print(num1,end=' ')
print(num2)

# Convert age from string to integer after using split().
name , age = input("Enter name and age : ").split()
print(age,type(age))
age = int(age)
print(age,type(age))