"""
Methods : 
        As we know set is mutable so we can easily add and remove the elements from set.
        So there are some built in methods has provided to work with set.
"""

"""
1.add() : add() method is used to add single element to set.
"""
s = {10,20,30,40,50}
print(s)
s.add(101)
print(s)

"""
2.update() : update() method is used to add other iterable objects like list,tuple,set to set.
"""
s = {10,20,30,40,50}
print(s)
s.update({101,201,301})
print(s)

"""
3.remove() : remove() method is used to remove the element from set and if element not found then it shows keyError
"""
s = {10,20,30,40,50}
print(s)
s.remove(20)
print(s)

"""
4.discard() : discard() method is used to remove the specified element from set and if element not found then set remains unchanged.
"""
s = {10,20,30,40,50}
print(s)
s.discard(20)
print(s)

"""
5.pop() : pop() method is used to remove and return any random element from set and if set is empty it shows an error.
"""
s = {10,20,30,"wel",40,50}
print(s)
print(s.pop())
print(s)

"""
6.clear() : clear() method is used to clear the set.
"""
s = {10,20,30,40,50}
print(s)
s.clear()
print(s)

"""
7.copy() : copy() method is used to create a shallow copy of set.
"""
s = {10,20,30,40}
print(s,id(s))
s_copy = s.copy()
print(s_copy,id(s_copy))

"""
8.union() : union() method is used to return all the unique elements from the sets.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.union(s2))
print(s1 | s2)

"""
9.intersection() : intersection() method is used to return all the common elements between both the sets.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.intersection(s2))
print(s1 & s2)

"""
10.intersection_update() : intersection_update() method compute the intersection between both the sets and update it to the calling sets.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.intersection_update(s2))
print(s1)

"""
11.difference() : difference() method is used to return the elements from set1 but not from set2.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.difference(s2))
print(s1 - s2)

"""
12.difference_update() : difference_update() method compute the difference between 2 sets and update it to the calling set.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
s1.difference_update(s2)
print(s1)

"""
13.symmetric_difference() : symmetric_difference() method is used to return the elements from set1 and set2 but except the intersection.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

"""
14.symmetric_difference_update() : symmetric_difference_update() method is used to compute the symmetric_difference() between both the sets and update it to the calling set.
"""
s1 = {11,22,33,44,55}
s2 = {44,55,66,77,88}
s1.symmetric_difference_update(s2)
print(s1)

"""
15.isdisjoint() : isdisjoint() method return True if both the sets don't have any common elements between them otherwise it return False.
"""
s1 = {11,22,33}
s2 = {44,55,66,77,88}
print(s1.isdisjoint(s2))

"""
16.issubset() : issubset() method return True if all the elements of set1 is present inside set2 otherwise it return False.
"""
s1 = {44,55}
s2 = {44,55,66,77,88}
print(s1.issubset(s2))

"""
17.issuperset() : issuperset() method return True if all the elements of set2 is present inside set1 otherwise it return False.
"""
s1 = {11,22,33,44,55}
s2 = {44,55}
print(s1.issuperset(s2))