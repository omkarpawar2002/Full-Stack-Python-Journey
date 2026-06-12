# Count the number of keys in a dictionary.
student = {
    "name":"ajay",
    "age":24,
    "city":"pune"
}
print(len(student.keys()))

# Count the number of values in a dictionary.
student = {
    "name":"ajay",
    "age":24,
    "city":"pune"
}
print(len(student.values()))

# Create a dictionary of student marks and display all students.
students = {
    "rohit":89,
    "anuj":67,
    "kirti":90
}
print(students)

# Calculate the sum of all values in a dictionary.
students = {
    "rohit":89,
    "anuj":67,
    "kirti":90
}
print(sum(students.values()))

# Find the highest value in a dictionary.
students = {
    "rohit":89,
    "anuj":67,
    "kirti":90
}
print(max(students.values()))

# Find the lowest value in a dictionary.
students = {
    "rohit":89,
    "anuj":67,
    "kirti":90
}
print(min(students.values()))

# Create a dictionary from two lists.
keys = ["one","two","three"]
values = [10,20,30]
print(dict(zip(keys,values)))

# Merge two dictionaries.
student = {
    "name":"ajay",
    "age":24,
    "city":"pune"
}
marks = {
    "physics":67,
    "chemistry":89
}
student.update(marks)
print(student)


# Count occurrences of words in a sentence.
string_input = input("Enter any input : ").split()
count_words = {}
for item in string_input:
    if(item not in count_words):
        count_words[item] = 1
    else:
        count_words[item] += 1
print(count_words)

# Store subject marks and calculate total marks.
marks = {
    "physics":67,
    "chemistry":89
}
print(sum(marks.values()))

# Store subject marks and calculate average marks.
marks = {
    "physics":67,
    "chemistry":89
}
print(sum(marks.values())/2)

# Create a phone book using a dictionary.
phone_book = {
    "rohit":"+91 8934783498",
    "anuja":"+91 7834098342"
}
print(phone_book)

# Search for a contact in a phone book.
phone_book = {
    "rohit":"+91 8934783498",
    "anuja":"+91 7834098342"
}
print("rohit" in phone_book)
print("Shreyas" not in phone_book)

# Update a contact number.
phone_book = {
    "rohit":"+91 8934783498",
    "anuja":"+91 7834098342"
}
print(phone_book)
phone_book["anuja"] = "+91 8828988989"
print(phone_book)

# Delete a contact from a phone book.
phone_book = {
    "rohit":"+91 8934783498",
    "anuja":"+91 7834098342"
}
print(phone_book)
phone_book.pop("rohit")
print(phone_book)

# Create a dictionary containing your name, age, and city.
data = {
    "name":"Mayur",
    "age":34,
    "city":"pune"
}
print(data)

# Create an empty dictionary using {}.
d = {}
print(d)

# Create an empty dictionary using dict().
d1 = dict()
print(d1)

# Print the type of a dictionary.
data = {
    "name":"Mayur",
    "age":34,
    "city":"pune"
}
print(type(data))

# Create a dictionary containing information about a car.
car_info = {
    "make":"Suzuki",
    "model":"m13",
    "year":2026
}
print(car_info)

# Access and print the value of a specific key.
car_info = {
    "make":"Suzuki",
    "model":"m13",
    "year":2026
}
print(car_info["make"])

# Try accessing a non-existing key and observe the error.
car_info = {
    "make":"Suzuki",
    "model":"m13",
    "year":2026
}
# print(car_info["color"]) # Here error occur