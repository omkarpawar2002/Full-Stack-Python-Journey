# Take 5 numbers in a list and print the largest.
li = [34,56,76,23,23]
print(max(li))

# Count how many times a number appears.
li = [10,45.34,True,"welcome",10,10]
print(li.count(10))

# Reverse a list without using reverse().
li = [10,45.34,True,"welcome"]
print(li)
print(li[::-1])

# Create a shopping list and add items dynamically.
shooping_list = []
num = int(input("How many items you want to add : "))
for i in range(num):
    item = input("Enter item : ")
    shooping_list.append(item)
print(shooping_list)

# Remove duplicate values from a list.
li = [10,20,30,10,10]
print(li)
new_li = []
for i in li:
    if(i not in new_li):
        new_li.append(i)
print(new_li)

# Find sum of all elements in a list.
li = [10,20,30,40]
print(sum(li))

# Find smallest element in a list.
li = [10,20,30,40]
print(min(li))

# Print all even numbers from a list.
li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    if(i % 2 == 0):
        print(i)

# Print all odd numbers from a list.
li = [1,2,3,4,5,6,7,8,9,10]
for i in li:
    if(i % 2 != 0):
        print(i)

# Create a nested list of students and marks.
students = [
    ["kiran",101],
    ["anuja",232]
]
print(students)