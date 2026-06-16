# Create a string containing your full name.
full_name = "Keshav Jha"
print(full_name)

# Print the first character of your name.
full_name = "Keshav Jha"
print(full_name[0])

# Print the last character of your name.
full_name = "Keshav Jha"
print(full_name[-1])

# Print the length of your name.
full_name = "Keshav Jha"
print(len(full_name))

# Print your name in uppercase.
full_name = "Keshav Jha"
print(full_name.upper())

# Print your name in lowercase.
full_name = "Keshav Jha"
print(full_name.lower())

# Print your name in title case.
full_name = "Keshav Jha"
print(full_name.title())

# Print the first 3 characters of your name.
full_name = "Keshav Jha"
print(full_name[:3])

# Print the last 3 characters of your name.
full_name = "Keshav Jha"
print(full_name[-3:])

# Reverse your name using slicing.
full_name = "Keshav Jha"
print(full_name[::-1])

# Count how many times "a" appears in "banana".
fruit = "banana"
print(fruit.count('a'))

# Check whether "Python" starts with "Py".
st = "Python"
print(st.startswith("Py"))

# Check whether "report.pdf" ends with ".pdf".
data = "report.pdf"
print(data.endswith(".pdf"))

# Replace "Java" with "Python" in a sentence.
st_input = "I am learn Java Programming Language"
print(st_input)
print(st_input.replace("Java","Python"))

# Split "Apple,Mango,Banana" using comma.
st = "Apple,Mango,Banana"
print(st.split(','))

# Join a list of fruits using "-".
li = ['Apple', 'Mango', 'Banana']
print(li)
print("-".join(li))

# Find the position of "Programming" in "Python Programming".
st = "Python Programming"
print(st.index("Programming"))

# Check whether "12345" contains only digits.
digit = "12345"
print(digit.isdigit())

# Check whether "Python123" is alphanumeric.
st = "Python123"
print(st.isalnum())

# Remove extra spaces from both sides of a string.
"""
Note : For Visual Understanding instead of space i used ==== this.
"""
st = "====welcome===="
print(st)
print(st.strip("="))