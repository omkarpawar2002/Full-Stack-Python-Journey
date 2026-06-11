# Create a set of five numbers.
numbers = {10,20,30,40,50}
print(numbers)

# Create a set containing your favorite fruits.
fruits = {"apple","mango"}
print(fruits)

# Print the type of a set.
fruits = {"apple","mango"}
print(type(fruits))

# Create an empty set.
names = set()
print(names)

# Add a new element to a set using add().
names = set()
names.add("Ruchika")
print(names)

# Add multiple elements using update().
names = set()
names.update({"Ruhi","Shivam","Anna"})
print(names)

# Remove an element using remove().
names = {"Ruhi","Shivam","Anna"}
names.remove("Ruhi")
print(names)

# Remove an element using discard().
names = {"Ruhi","Shivam","Anna"}
names.discard("Anna")
print(names)

# Remove a random element using pop().
names = {"Ruhi","Shivam","Anna"}
names.pop()
print(names)

# Clear all elements from a set.
names = {"Ruhi","Shivam","Anna"}
names.clear()
print(names)

# Find the length of a set.
names = {"Ruhi","Shivam","Anna"}
print(len(names))

# Check whether a value exists using in.
names = {"Ruhi","Shivam","Anna"}
print("Ruhi" in names)
print("Keshav" in names)

# Check whether a value does not exist using not in.
names = {"Ruhi","Shivam","Anna"}
print("Ruhi" not in names)
print("Keshav" not in names)

# Convert a list into a set.
li = [11,22,33]
print(li)
s = set(li)
print(s)

# Convert a set into a list.
s = {10,20,30,40}
print(s)
li = list(s)
print(li)