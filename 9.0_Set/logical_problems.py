# Remove duplicate values from a list using a set.
li = [11,22,22,33]
print(li)
s = set(li)
li = list(s)
print(li)

# Count the number of unique values in a list.
li = [11,22,22,33]
s = set(li)
li = list(s)
print(len(li))

# Find common elements between two sets.
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1 & s2)

# Find all unique elements from two sets.
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1 | s2)

# Find elements present in the first set but not in the second.
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1 - s2)

# Find elements present in either set but not both.
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1 ^ s2)

# Check whether one set is a subset of another.
s1 = {44,55}
s2 = {44,55,66,77,88}
print(s1.issubset(s2))

# Check whether one set is a superset of another.
s1 = {44,55}
s2 = {44,55,66,77,88}
print(s2.issuperset(s1))

# Check whether two sets are disjoint.
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.isdisjoint(s2))

# Create a set of squares from 1 to 10 using set comprehension.
squares = {i**2 for i in range(1,11)}
print(squares)

# Compare two sets and determine whether they are equal.
s1 = {44,55}
s2 = {44,55}
print(s1 == s2)

# Create a set from user input.
names = set()
for i in range(3):
    name = input("Enter any name : ")
    names.add(name)
print(names)

# Count unique characters in a string.
st = "welcome"
count_string = set(st)
print(len(count_string))

# Find common characters between two strings using sets.
st1 = "welcome"
st2 = "listen"
s1 = set(st1)
s2 = set(st2)
print(s1 & s2)

# Find duplicate values from a list using sets.
li = [99,88,77,66,55,55,44,55,33]
print(li)
unique_values = set()
duplicate_values = set()
for i in li:
    if(i not in unique_values):
        unique_values.add(i)
    else:
        duplicate_values.add(i)
print("Duplicate Values : ",duplicate_values)

# Create a frozenset.
roles = {"admin","manager","hr"}
confirm_roles = frozenset(roles)
print(confirm_roles)

# Attempt to modify a frozenset and observe the error.
roles = {"admin","manager","hr"}
confirm_roles = frozenset(roles)
print(confirm_roles)
# confirm_roles.add(23)  # This line will make an AttributeError

# Find unique vowels in a string.
string_input = "welcome"
s = {i for i in string_input if(i in 'aeiouAEIOU')}
print(s)
