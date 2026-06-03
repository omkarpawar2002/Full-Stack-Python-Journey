# Variable 
'''
Variable is a container which is used to store or hold a value so we can reuse it later.
or we can say 
variable is a name that refers to an object (value) in memory.
'''

# How do we create a variable in python
'''
syntax :  variable_name = Value

Example : name = "ashok"    

1. name is a variable
2. "ashok" is a value
3. = is an assignment operator which is used to assign the right hand side value to the left hand side of variable
'''

# Rules for defining a variable name in python
'''
1.Variable name should start with a letter or underscore.
        age = 34
        _isavailable = True

2.Variable name not start with a number.
        1name = "kirti"  # This is wrong

3.Variable name can contain alphanumeric character.
        name_1 = "narayan"

4.Among all the special character only underscore is allowed.
        last_name = "Kumar"     # valid 
        first$name = "kiran"    # Invalid

5.Variable name are case sensitive.
        age = 34
        Age = 45    # These both are different 

6.Reserved keywords can not be used as a variable name in python.
        if = 34  # Invalid because if have a special meaning in python programming language.
'''

# Valid or Invalid variable names
'''
    Valid Variable              Invalid Variable

        name_1                      1_name
        full_name                   full$name
        firstname                   first name
'''

# Dynamic typing 
'''
1.There are actually 2 types of programming languages statically typed or dynamically typed.
2.So python is a dynamically typed programming language.
3.In other programming language like c , c++ or java before defining a variable we need to specify the data type means which kind of data that we are going to store in a variable.
4.But here in python we no need to specify the data type during runtime python will automatically find which type of data it is.
5.In java we define variable like this  : int age = 34
6.In python we define variable like this : age = 34
'''

# Assigning values
'''
1.Here = is an assignment operator which assign the RHS value to the LHS of variable.
2.Example : first_name = "nurr"
'''

# Assign multiple values in same line 
'''
a,b,c = 10,20,30
print(a)
print(b)
print(c)
'''

# Assign same value to the multiple variable
'''
a = b = c = 30
print(a)
print(b)
print(c)
'''

# Reassign variables
'''
Yes , we can reassign the values to variables.

age = 34
print(age)
age = 52
print(age)
'''

# Constant convention
'''
1.In other programming language like c if we want a variable value not be change throught the program so we make the variable constant by using the const keyword.
2.But here in python there is now way to make a variable constant.
3.If you want to tell other programmer about email variable will be constant so try to write the variable name in uppercase like EMAIL this. So it's a hint to other try to not modify value but yes we can.
4.Example :
            EMAIL = "youremail@gmail.com"
            PI = 3.14
'''