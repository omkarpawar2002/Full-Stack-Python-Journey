# Print numbers from 1 to 10 using a loop.
for i in range(1,11):
    print(i)

# Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

# Print all even numbers from 1 to 20.
for i in range(1,21):
    if(i % 2 == 0):
        print(i)

# Print all odd numbers from 1 to 20.
for i in range(1,21):
    if(i % 2 != 0):
        print(i)

# Print each character of a string.
st = "welcome"
for i in st:
    print(i)

# Print each item of a list.
li = [11,22,33,44]
for i in li:
    print(i)

# Count from 1 to 5 using a while loop.
count = 1
while count < 6:
    print(count)
    count += 1

# Print a name 5 times.
name = "diksha"
for i in range(5):
    print(name)

# Find the sum of numbers from 1 to 10.
total = 0
for i in range(1,11):
    total += i
print("Total : ",total)

# Find the sum of even numbers from 1 to 20.
total = 0
for i in range(1,21):
    if(i % 2 == 0):
        total += i
print("Total : ",total)

# Print the square of numbers from 1 to 10.
for i in range(1,11):
    print(i ** 2)

# Print numbers divisible by 5 from 1 to 50.
for i in range(1,51):
    if(i % 5 == 0):
        print(i)

# Stop a loop when a specific number is reached.
for i in range(1,11):
    if(i == 3):
        break
    print(i)

# Skip a specific number while printing.
for i in range(1,11):
    if(i == 3):
        continue
    print(i)

# Print a countdown timer.
count = 10
while count > 0:
    print(count)
    count -= 1

# Count vowels in a string.
st = input("Enter any input : ")
count_vowel = 0
for i in st:
    if(i in 'aeiouAEIOU'):
        count_vowel += 1
print("Total Vowels :",count_vowel)

# Print the length of a string using a loop.
st = input("Enter any input : ")
count_length = 0
for i in st:
    count_length += 1
print("Length :",count_length)

# Print numbers in reverse order.
for i in range(10,0,-1):
    print(i)

# Print a multiplication table using loops./
num = int(input("Enter any number : "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

# Create a simple menu that runs until the user chooses Exit.
num = int(input("Enter any number : "))
while num != 0:
    num = int(input("Enter any number : "))