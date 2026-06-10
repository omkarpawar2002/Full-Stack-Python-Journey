# Methods :
"""
As we know list are mutable means once we create a list so we can easily update or remove the elements from list by using the built-in methods.
"""

"""
1.append() : append() method is used to add single element to the end of list.
"""
li = [10,20,30,40]
print(li)
li.append(101)
print(li)


"""
2.extend() : extend() method is used to add multiple elements from other iterable object like list,tuple,set etc., to the end of list.
"""
li = [10,20,30,40]
print(li)
li.extend([101,201,301])
print(li)


"""
3.insert() : insert() method is used to add single element at specified index position.
"""
li = [10,20,30,40]
print(li)
li.insert(0,101)
print(li)


"""
4.remove() : remove() method is used to remove the first occurance of specified element from list and if the element not found then it shows valueError.
"""
li = [10,10,20,30,40]
print(li)
li.remove(10)
print(li)


"""
5.pop() : pop() method is used to remove and return last element from list and if list is empty it shows an indexError.
"""
li = [10,10,20,30,40]
print(li)
print(li.pop())
print(li)


"""
6.pop(index) : pop(index) method is used to remove and return the element from specified index position and if list is empty it shows an indexError.
"""
li = [10,10,20,30,40]
print(li)
print(li.pop(2))
print(li)


"""
7.clear() : clear() method is used to clear all the elements from list.
"""
li = [10,10,20,30,40]
print(li)
li.clear()
print(li)


"""
8.reverse() : reverse() method is used to reverse the list.
"""
li = [10,10,20,30,40]
print(li)
li.reverse()
print(li)


"""
9.index() : index() method is used to return the index position of first occurance of specified element in list and if element not present then it shows valueError.
"""
li = [10,10,20,30,40]
print(li)
print(li.index(301))


"""
10.count() : count() method is used to return the total count of occurance of specified element in list.
"""
li = [10,10,20,30,40]
print(li)
print(li.count(10))


"""
11.copy() : copy() method is used to create a shallow copy of list and it creates a independant copy of list.
"""
li = [10,10,20,30,40]
print(li,id(li))
li_copy = li.copy()
print(li_copy,id(li_copy))


"""
12.sort() : sort() method is used to sort the list either in assending or descending order.
            In descending order put reverse = True.
"""
li = [10,14,354,12,1,3,677]
print(li)
li.sort()
print(li)