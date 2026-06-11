# Count how many times a number appears in a tuple.
numbers = (10,20,30,10,10,10,40,50)
print(numbers.count(10))

# Find the index of a given value.
numbers = (10,20,30,10,10,10,40,50)
print(numbers.index(10))

# Check whether a value exists in a tuple.
numbers = (10,20,30,40,50)
print(20 in numbers)

# Find the largest number in a tuple.
numbers = (10,20,30,40,50)
print(max(numbers))

# Find the smallest number in a tuple.
numbers = (10,20,30,40,50)
print(min(numbers))

# Calculate the sum of all tuple elements.
numbers = (10,20,30,40,50)
print(sum(numbers))

# Count even numbers in a tuple.
t = (1,2,3,4,5,6,7,8,9,10)
count_even = 0
for i in t:
    if(i % 2 == 0):
        count_even += 1
print(count_even)

# Count odd numbers in a tuple.
t = (1,2,3,4,5,6,7,8,9,10)
count_odd = 0
for i in t:
    if(i % 2 != 0):
        count_odd += 1
print(count_odd)

# Print all elements using a loop.
t = (1,2,3,4,5,6,7,8,9,10)
for i in t:
    print(i,end=' ')

# Create a tuple and display elements in reverse order.
t = (1,2,3,4,5,6,7,8,9,10)
print()
for i in reversed(t):
    print(i,end=' ')

# Slice first half of tuple.
t = (10,20,30,40,50)
print(t[:3])

# Slice second half of tuple.
t = (10,20,30,40,50)
print(t[2:])

# Create tuple of names and search a name.
names = ("om","shim","yami")
name = input("Enter name : ")
print(name in names)

# Merge two tuples.
t1 = (10,20,30)
t2 = ("om","df")
print(t1 + t2)

# Repeat a tuple three times.
t = (10,20,30)
print(t * 3)

# Sort tuple values.
t = (10,45,23,56,7)
li = list(t)
li.sort()
t = tuple(li)
print(t)

# Convert tuple to list.
t = (10,20,30,40)
print(t)
li = list(t)
print(li)

# Convert list to tuple.
t = ["on1","off2"]
print(t)
li = tuple(t)
print(li)