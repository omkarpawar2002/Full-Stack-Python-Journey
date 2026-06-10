# List Data Structure :
"""
List is a mutable,ordered collection of data structure which used to store collection of elements seperated by comma inside square bracket [].
"""

# What is a data structure :
"""
A data structure is a way of organizing, storing, and managing data so it can be accessed and modified efficiently.
"""

# Why we required a list data structure :
"""
1.As we know to store a value we used variable but they are only able to hold single value.
2.What if i want to store 100 student name so it does not make sense to create 100 variable and store their name.
3.Instead of these we can create a variable name which means list object and store 100 student name.
"""

# Properties Of Lists :
"""
1.List is mutable in nature.
2.List is represented by square bracket [].
3.List allow to store heterogenous data.
4.List allow to store duplicate elements.
5.List allow indexing [both positive and negative].
6.List also supports slicing.
"""

# How to create a list :
"""
There are 2 ways to create a list in python :
    1.by using empty square bracket 
        E.g., li = []

    2.by using list() function 
        E.g., li = list()
"""

# List allows to store heterogenous data :
li = [10,20,True,"welcome",45.67]
print(li)

# List allows to store duplicate elements :
li = [10,10,20,30,10]
print(li)

# List allows indexing [both positive and negative] :
"""
Indexing : Indexing is a position of which was given to every element in list.
           Positive Indexing starts from 0 not with 1 and Negative Indexing starts with -1.
"""
li = [10,20,True,"welcome",45.67]
print("Positive Indexing")
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])

print()

print("Negative Indexing")
print(li[-1])
print(li[-2])
print(li[-3])
print(li[-4])
print(li[-5])

# List supports slicing :
"""
slicing : slicing means to break down the sequence into subsequences.
"""
li = [10,20,30,40,50]
print(li[:4])
print(li[1:3])

# List is mutable :
"""
Mutable means once created can be changed.
"""
li = [10,20,30]
print(li)
li[1] = 101
print(li)

# Nested List :
"""
When list inside another list is known as nested list in python.
"""
li = [["Mumbai","Pune"],["surat","jamnagar"]]
print(li)
print(li[0])
print(li[1])
print(li[0][0])
print(li[1][-1])

# How to change list elements :
li = [10,20,30,40]
print(li)
li[3] = 101
print(li)