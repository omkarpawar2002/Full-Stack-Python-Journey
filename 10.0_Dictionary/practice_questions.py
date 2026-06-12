# Create a student dictionary.
student = {
    "name":"Kiran",
    "age":23
}
print(student)

# Create an employee dictionary.
employee = {
    "emp_id":34563412,
    "emp_name":"Nirmala",
    "emp_dept":"Hr"
}
print(employee)

# Access values using keys.
student = {
    "name":"Kiran",
    "age":23
}
print(student["name"])

# Add a new key-value pair.
student = {
    "name":"Kiran",
    "age":23
}
student["city"] = "pune"
print(student)

# Update an existing value.
student = {
    "name":"Kiran",
    "age":23
}
student["age"] = 35
print(student)

# Delete a key using pop().
student = {
    "name":"Kiran",
    "age":23
}
student.pop("name")
print(student)

# Delete the last item using popitem().
student = {
    "name":"Kiran",
    "age":23
}
student.popitem()
print(student)

# Display all keys.
student = {
    "name":"Kiran",
    "age":23
}
print(student.keys())

# Display all values.
student = {
    "name":"Kiran",
    "age":23
}
print(student.values())

# Display all key-value pairs.
student = {
    "name":"Kiran",
    "age":23
}
print(student.items())

# Create a copy of a dictionary.
student = {
    "name":"Kiran",
    "age":23
}
print(student,id(student))
stu_copy = student.copy()
print(stu_copy,id(stu_copy))

# Clear a dictionary.
student = {
    "name":"Kiran",
    "age":23
}
student.clear()
print(student)

# Use get() with an existing key.
student = {
    "name":"Kiran",
    "age":23
}
print(student.get("name"))

# Use get() with a missing key.
student = {
    "name":"Kiran",
    "age":23
}
print(student.get("city"))

# Use setdefault() with an existing key.
student = {
    "name":"Kiran",
    "age":23
}
print(student.setdefault("name","arpita"))
print(student)

# Use setdefault() with a new key.
student = {
    "name":"Kiran",
    "age":23
}
print(student.setdefault("city","pune"))
print(student)

# Create a dictionary using fromkeys().
subjects = ["phy","chem","math"]
stu_marks = dict.fromkeys(subjects,0)
print(stu_marks)

# Check if a key exists.
student = {
    "name":"Kiran",
    "age":23
}
print("age" in student)

# Check if a key does not exist.
student = {
    "name":"Kiran",
    "age":23
}
print("age" not in student)

# Loop through dictionary keys.
student = {
    "name":"Kiran",
    "age":23
}
for item in student.keys():
    print(item)

# Loop through dictionary values.
student = {
    "name":"Kiran",
    "age":23
}
for item in student.values():
    print(item)

# Loop through dictionary items.
student = {
    "name":"Kiran",
    "age":23
}
for key,value in student.items():
    print(key,"==",value)

# Create a nested dictionary of students.
students = {
    101 : {
        "name":"kiran",
        "age":34
    },
    102 : {
        "name":"aayush",
        "age":23
    }
}
print(students)

# Access values from a nested dictionary.
students = {
    101 : {
        "name":"kiran",
        "age":34
    },
    102 : {
        "name":"aayush",
        "age":23
    }
}
print(students[101]["name"])
print(students[102]["age"])

# Update values inside a nested dictionary.
students = {
    101 : {
        "name":"kiran",
        "age":34
    },
    102 : {
        "name":"aayush",
        "age":23
    }
}
students[101]["age"] = 25
print(students)

# Create a dictionary of numbers and their squares.
squares = {i:i**2 for i in range(1,11)}
print(squares)

# Create a dictionary from a list of names and their lengths.
names = ["kiran","prajakta","janhvai"]
names_length = dict.fromkeys(names,0)
names_length["kiran"] = len("kiran")
names_length["prajakta"] = len("prajakta")
names_length["janhvai"] = len("janhvai")
print(names_length)

# Count frequency of characters in a string.
st = "welcome"
count_char = {}
for item in st:
    if(item not in count_char):
        count_char[item] = 1
    else:
        count_char[item] += 1
print(count_char)