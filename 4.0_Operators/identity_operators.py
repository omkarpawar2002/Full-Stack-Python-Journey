# Identity Operators :
'''
Identity Operators are used to check whether both objects / variable point to the same memory location or not.

There are 2 types of identity operators :
    1.is
    2.is not
'''

# is operator :
'''
is operator return True if both objects/variables are point to the same memory location , otherwise they return False
'''
a = 10
b = 10
print(a is b)

# is not operator :
'''
is not operator return True if both objects/variables are not point to the same memory location , otherwise they return False
'''
a = [10,20,30]
b = [10,20,30]
print(a is not b)