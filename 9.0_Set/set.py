# Set Data Structure :
"""
Set is a mutable, unordered collection of unique elements.

Properties Of Sets :
1.Set is mutable in nature.
2.Set can store only immutable elements.
3.Set is represented by curly brackets {}.
4.Set does not maintain the insertion order.
5.Set does not allow to store duplicate elements.
6.set does not supports slicing or indexing.
"""

# How to create an empty set in python 
"""
s = set()
"""

# Set is unordered data structure.
s = {10,20,30,"welcome"}
print(s)

# Set does not allow duplicate values.
s = {10,20,30,30,30,30}
print(s)

# Set is used to store unique values and faster in membership tesing.
s = {10,20,30,40,50,60}
print(10 in s)

# frozenset() :
"""
A frozenset is an immutable version of a set. It is used when we need unique values that should not be modified after creation. Since it is immutable, it can also be used inside sets and as dictionary keys, unlike normal sets.
"""
s = {11,22,33,44}
print(s)
s.add(101)
print(s)

s1 = frozenset({11,22,33,44})
print(s1)
s1.add(202) # here we get an attributeError.
print(s1)