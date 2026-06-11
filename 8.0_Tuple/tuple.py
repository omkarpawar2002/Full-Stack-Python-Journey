# Tuple Data Structure :

"""
Tuple is one of the python built-in data structure which used to store collection of elements seperated by comma inside paranthesis ().

Tuple Properties :
1.Tuple is immutable in nature.
2.Tuple is represented by paranthesis ().
3.Tuple allow to store heterogenous data.
4.Tuple allow to store duplicate values.
5.Tuple allows indexing.
6.Tuple also supports slicing.
"""

# Why we required a Tuple data structure :
"""
1.As we know to store a value we used variable but they are only able to hold single value.
2.But tuple is immutable so we only store the data in tuple that never change in future.
3.E.g., birth_date , co-ordinates , rgb_color_values etc..,
"""


# How to create a tuple :
"""
There are 2 ways to create a tuple in python :
    1.by using empty paranthesis 
        E.g., t = ()

    2.by using tuple() function 
        E.g., t = tuple()
"""

# tuple allows to store heterogenous data :
t = (10,20,True,"welcome",45.67)
print(t)

# Tuple allows to store duplicate elements :
t = (10,10,20,30,10)
print(t)

# Tuple allows indexing [both positive and negative] :
"""
Indexing : Indexing is a position of which was given to every element in Tuple.
           Positive Indexing starts from 0 not with 1 and Negative Indexing starts with -1.
"""
t = (10,20,True,"welcome",45.67)
print("Positive Indexing")
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])

print()

print("Negative Indexing")
print(t[-1])
print(t[-2])
print(t[-3])
print(t[-4])
print(t[-5])

# Tuple supports slicing :
"""
slicing : slicing means to break down the sequence into subsequences.
"""
t = (10,20,30,40,50)
print(t[:4])
print(t[1:3])

# Tuple is immutable :
"""
Immutable means once created cannot be changed.
"""
t = (10,20,30)
print(t)
# t[0] = 101 It will show an error

# Nested Tuple :
"""
When Tuple inside another Tuple is known as nested Tuple in python.
"""
t = (("Mumbai","Pune"),("surat","jamnagar"))
print(t)
print(t[0])
print(t[1])
print(t[0][0])
print(t[1][-1])

# packing : 
"""
The term packing referes to put multiple values into a tuple.
"""
a = 10 
b = 10
t = (a,b)
print(t)

# unpacking :
"""
The term unpacking referes to put multiple values of tuple into different variable.
"""
t = (10,20,30)
a,b,c = t
print(a)
print(b)
print(c)

# To create a tuple of single element :
"""
If we not put comma then it will be treated as a integer but when we put comma then it will be treated as a tuple . Comma is very important because tuple identifies based on comma not with paranthesis.
"""
t = (10)
print(t,type(t))
t = (10,)
print(t,type(t))