# Create a tuple of five numbers.
numbers = (10,20,30,40,50)
print(numbers)

# Create a tuple containing your name, age and city.
data = ("kiran",32,"pune")
print(data)

# Create a single-element tuple.
t = (10,)
print(t,type(t))

# Print the first item of a tuple.
numbers = (10,20,30,40,50)
print(numbers[0])

# Print the last item using negative indexing.
numbers = (10,20,30,40,50)
print(numbers[-1])

# Create a tuple using packing.
name , age  = "nirmla",23
t = (name,age)
print(t)

# Unpack a tuple into three variables.
data = (10,"welcome",34.23)
a,b,c = data
print(a,b,c)

# Print the second element of a tuple.
numbers = (10,20,30,40,50)
print(numbers[1])

# Slice the first three elements from a tuple.
numbers = (10,20,30,40,50)
print(numbers[:3])

# Slice the last two elements from a tuple.
numbers = (10,20,30,40,50)
print(numbers[3:])