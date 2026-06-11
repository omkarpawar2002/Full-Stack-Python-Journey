# Methods : 
"""
1.As we know tuple is immutable in nature so once we created a tuple can not be change.
2.So in short we can say we used tuple for only reading purpose.
3.So tuple only provide 2 built in methods.
"""

"""
1.count() : count() method is used to return the total count of occurance of specified element in tuple.
"""
t = (10,20,30,10,10)
print(t.count(10))

"""
2.index() : index() method is used to return the index position of first occurance of specified element in tuple and if element not found then it shows valueError.
"""
t = (10,20,30,40,50)
print(t.index(101))