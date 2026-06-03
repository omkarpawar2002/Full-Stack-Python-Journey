# Data types
'''
Data types actually tell us which kind of data variable holds.

There are different types of data types in python 
    1.Fundamental data types :  These data type only able to hold a single value

    2.Collective data types : These data type hold collection of values or multiple values.
'''

# 1.Int data type
'''
    It holds a whole number
'''
age = 23
roll_no = 101

# 2.Float data type
'''
    It holds number with decimal parts
'''
marks = 34.89
temperature = 37.3

# 3.Complex data type
'''
    A complex number consists of a real part and an imaginary part.
    These data type used in scientific calculation or complex mathematics.
'''
data = 1 + 2j

# 4.Boolean data type
'''
    Boolean data type contain only True or False this 2 values only.
'''
is_user_login = True
is_available = False

# 5.String data type
'''
    String is a sequence of characters.
'''
name = "kirti"

# 6.List data type
'''
    List is mutable and used to store collection of values inside [].
'''
stu_roll = [101,102,103,104,105]

# 7.Tuple data type
'''
    Tuple is immutable and used to store collection of values inside ().
'''
email = ('kirti@123gmail.com','suman@12gmail.com')

# 8.Set data type
'''
    Set is mutable,unordered collection of data structure used to store unique elements inside {}.
'''
numbers = {1,2,2,2,4}
print(numbers)  # {1,2,4}

# 9.Dictionary data type
'''
    Dictionary is mutable and used to store data in form of key:value pairs inside {}.
'''
user_details = {
    'name':'mohan',
    'age':23,
    'location':'Delhi'
}

# 10.None data type
'''
    It represents nothing which means absence of a value.
'''
user_detail = None