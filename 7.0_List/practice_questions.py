# Create a list of 5 fruits and print it.
fruits = ["apple","banana","grapes","mango","pinapple"]
print(fruits)

# Create an empty list.
li = []
print(li)

# Create a mixed data type list.
li = [10,45.34,True,"welcome"]
print(li)

# Print the first element of a list.
li = [10,45.34,True,"welcome"]
print(li[0])

# Print the last element using negative indexing.
li = [10,45.34,True,"welcome"]
print(li[-1])

# Find length of a list.
li = [10,45.34,True,"welcome"]
print(len(li))

# Add an item using append().
li = [10,45.34,True,"welcome"]
print(li)
li.append(101)
print(li)

# Add multiple items using extend().
li = [10,45.34,True,"welcome"]
print(li)
li.extend(["first","second","third"])
print(li)

# Insert an item at index 2.
li = [10,45.34,True,"welcome"]
print(li)
li.insert(2,101)
print(li)

# Remove an item using remove().
li = [10,45.34,True,"welcome"]
print(li)
li.remove(45.34)
print(li)