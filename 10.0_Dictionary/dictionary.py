# Dictionary Data Structure :
"""
Dictionary is one of the python built-in data structure.
Dictionary is used to store collection of key-value pairs.

Properties Of Dictionary :
1.Dictionary is mutable in nature.
2.Dictionary is represented by curly brackets {}.
3.Data in dictionary store in key:value pairs form.
4.After python 3.7+ Dictionary maintain the insertion order.
5.Dictionary keys must be hashable (typically immutable types like int, str, tuple).
Values can be of any type.
6.We store data in dictionary key:value pairs form so indexing and slicing is not possible.
"""

# Create a Dictionary :
"""
There are two ways to create a dictionary :
    1.d = {}

    2.d = dict()
"""

# Example :
student = {
    "name":"Vikas",
    "age":23
}
print(student)

# How to access value in dictionary 
student = {
    "name":"Vikas",
    "age":23
}
print(student["age"]) # Here we get value of age key.
# print(student["city"]) # Here we get an error because city key not present in dictionary

# Here we see how to modify existing value in dictionary
student = {
    "name":"Vikas",
    "age":23
}
student["age"] = 19
print(student)

# Here we see how to add new key:Value pair to dictionary
student = {
    "name":"Vikas",
    "age":23
}
student["city"] = "kalyan"
print(student)

# If we provide same key again then new value will override the old value.
student = {
    "name":"Vikas",
    "age":23,
    "name":"nirmala"
}
print(student)

# To check key exist in dictionary or not
student = {
    "name":"Vikas",
    "age":23
}
print("age" in student)
print("city" not in student)

# How to loop over dictionary keys 
student = {
    "name":"Vikas",
    "age":23
}
for item in student:
    print(item)

for item in student.keys():
    print(item)

# How to loop over dictionary values
student = {
    "name":"Vikas",
    "age":23
}
for value in student.values():
    print(value)

# How to loop over key:value pair dictionary
for key,value in student.items():
    print(key,value)