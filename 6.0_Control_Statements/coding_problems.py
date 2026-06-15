# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

# Print numbers from 1 to 20 using a while loop.
i = 1
while i < 21:
    print(i)
    i += 1

# Print all even numbers from 1 to 50.
for i in range(1,51):
    if(i % 2 == 0):
        print(i)

# Print all odd numbers from 1 to 50.
for i in range(1,51):
    if(i % 2 != 0):
        print(i)

# Print the square of numbers from 1 to 10.
for i in range(1,11):
    print(i**2)

# Print the cube of numbers from 1 to 10.
for i in range(1,11):
    print(i**3)

# Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

# Print numbers divisible by 3 from 1 to 30.
for i in range(1,31):
    if(i % 3 == 0):
        print(i)

# Print numbers divisible by 5 from 1 to 50.
for i in range(1,51):
    if(i % 5 == 0):
        print(i)

# Print all characters of a user-entered string.
st = input("Enter any input :- ")
for i in st:
    print(i)

# Print numbers from 1 to 20 and stop when 10 is reached.
for i in range(1,21):
    print(i)
    if(i == 10):
        break

# Ask for a password repeatedly until the correct password is entered.
while True:
    password = input("Enter password :- ")
    if(password == "admin"):
        print("Correct Password!!")
        break
    else:
        print("Incorrect Password!!")

# Search for a number in a list and stop when found.
numbers = [11,22,33,44,55,66]
num = 44
for i in numbers:
    print(i)
    if(i == num):
        break

# Print numbers from 1 to 20 except 10.
for i in range(1,21):
    if(i == 10):
        continue
    print(i)

# Print all numbers from 1 to 30 except multiples of 3.
for i in range(1,31):
    if(i % 3 == 0):
        continue
    print(i)

# Print all characters of a string except vowels.
st = "programming"
for i in st:
    if(i not in "aeiou"):
        print(i)

# Print a countdown from 20 to 1.
count = 20
while count > 0:
    print(count)
    count -= 1

# Calculate the sum of numbers from 1 to N.
num = int(input("Enter any numbers :- "))
print(f"Sum of 1 to {num} is : {sum(list(range(1,num+1)))}")

# Print a multiplication table using a while loop.
i = 1
num = int(input("Enter any number :- "))
while i < 11:
    print(f"{num} * {i} = {num * i}")
    i += 1

# Print a 5 × 5 grid of stars.
# Expected Output:

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(1,6):
    for j in range(1,6):
        print("*",end=' ')
    print()