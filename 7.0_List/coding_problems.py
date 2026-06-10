# Create a list of 5 numbers.
numbers = [10,20,30,40,50]
print(numbers)

# Print first and last element.
numbers = [10,20,30,40,50]
print(numbers[0],numbers[-1])

# Print all elements using loop.
numbers = [10,20,30,40,50]
for num in numbers:
    print(num)

# Add a new element using append().
numbers = [10,20,30,40,50]
print(numbers)
numbers.append(101)
print(numbers)

# Insert an element at specific position.
numbers = [10,20,30,40,50]
print(numbers)
numbers.insert(1,201)
print(numbers)

# Remove an element by value.
numbers = [10,20,30,40,50]
print(numbers)
numbers.remove(20)
print(numbers)

# Remove an element by index.
numbers = [10,20,30,40,50]
print(numbers)
numbers.pop(2)
print(numbers)

# Count occurrences of a number.
numbers = [10,20,30,40,50]
print(numbers)
print(numbers.count(20))

# Sort list ascending.
numbers = [56,34,56,78,34]
numbers.sort()
print(numbers)

# Sort list descending.
numbers = [56,34,56,78,34]
numbers.sort(reverse=True)
print(numbers)

# Reverse a list.
numbers = [10,20,30,40,50]
print(numbers)
numbers.reverse()
print(numbers)

# Copy a list.
numbers = [10,20,30,40,50]
print(numbers,id(numbers))
num_copy = numbers.copy()
print(num_copy,id(num_copy))

# Create a nested list.
state = [['Bihar','Punjab'],['Maharashtra','Madhya Pradesh']]
print(state)

# Access element from nested list.
state = [['Bihar','Punjab'],['Maharashtra','Madhya Pradesh']]
print(state[0][0])
print(state[1][-1])

# Find largest number.
numbers = [10,20,30,40,50]
print(max(numbers))

# Find smallest number.
numbers = [10,20,30,40,50]
print(min(numbers))

# Find sum of list elements.
numbers = [10,20,30,40,50]
print(sum(numbers))

# Find average of list elements.
numbers = [10,20,30,40,50]
print(sum(numbers)/5)

# Take 5 names and store in list.
names = []
for i in range(5):
    name = input("Enter your name : ")
    names.append(name)
print(names)

# Build a simple shopping list program.
shooping_list = []
num = int(input("How many elements you want to buy : "))
for i in range(num):
    name = input("Enter any item : ")
    shooping_list.append(name)
print("I want to purchase this items : ")
for item in shooping_list:
    print(item)