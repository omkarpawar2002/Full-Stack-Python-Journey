# Methods :
"""
Methods are built in functions used to format the strings.
"""

"""
1.lower() : lower() method is used to convert the string into lowercase.
"""
st = "hello world"
print(st)
print(st.lower())

"""
2.upper() : upper() method is used to convert the string into uppercase.
"""
st = "hello world"
print(st)
print(st.upper())

"""
3.title() : title() method is used to convert first letter of every word in uppercase.
"""
st = "hello world"
print(st)
print(st.title())

"""
4.capitalize() : capitalize() method is used to convert the first character in uppercase and rest of them in lowercase.
"""
st = "hello World"
print(st)
print(st.capitalize())

"""
5.len() : len() function is used to return the total length of string.
"""
st = "hello world"
print(len(st))

"""
6.isalpha() : isalpha() method return True only if string contain only alphabets otherwise it return False.
"""
st = "helloworld"
print(st)
print(st.isalpha())

"""
7.isdigit() : isdigit() method return True only if string contain only digits otherwise it return False.
"""
st = "123345"
print(st)
print(st.isdigit())

"""
8.isalnum() : isalnum() method return True if string contains only alphabets and/or digits (no spaces or special characters) otherwise they return False.
"""
st = "helloworld123"
print(st)
print(st.isalnum())

"""
9.isspace() : isspace() method return True only if string contain only space otherwise it return False.
"""
st = "  "
print(st)
print(st.isspace())

"""
10.islower() : islower() method return True only if string is in lowercase otherwise it return False.
"""
st = "hello world"
print(st)
print(st.islower())

"""
11.isupper() : isupper() method return True only if string is in uppercase otherwise it return False.
"""
st = "HELLO WORLD"
print(st)
print(st.isupper())

"""
12.startswith() : startswith() method return True if string starts with specified substring otherwise it return False.
"""
st = "hello world"
print(st)
print(st.startswith('h'))

"""
13.endswith() : endswith() method return True if string ends with specified substring otherwise it return False.
"""
st = "hello world"
print(st)
print(st.endswith('d'))

"""
14.lstrip() : lstrip() method is used to remove white spaces from left side of string.
"""
st = "=====welcome====="
print(st)
print(st.lstrip("="))

"""
15.rstrip() : rstrip() method is used to remove white spaces from right side of string.
"""
st = "=====welcome====="
print(st)
print(st.rstrip("="))

"""
16.strip() : strip() method is used to remove white spaces from both side of string.
"""
st = "=====welcome====="
print(st)
print(st.strip("="))

"""
17.count() : count() method is used to return Total count of occurance of specified substring in a string.
"""
st = "Hello World"
print(st)
print(st.count('l'))

"""
18.index() : index() method return the index position of specified substring in a string and if the specified substring is not found in string then it return valueError.
"""
st = "Hello World"
print(st)
print(st.index('l'))

"""
19.rindex() : rindex() method return the highest index position of specified substring in a string and if the specified substring is not found in string then it return valueError.
"""
st = "Hello World"
print(st)
print(st.rindex('l'))

"""
20.find() : find() method return the index position of specified substring in a string and if the specified substring is not present in string then it return -1.
"""
st = "Hello World"
print(st)
print(st.find('z'))

"""
21.rfind() : rfind() method is used to return the highest index position of specified substring in a string and if the specified substring is not found in string then it return -1.
"""
st = "Hello World"
print(st)
print(st.rfind('l'))
print(st.rfind('z'))

"""
22.replace() : replace() method is used to replace old value with new value.
"""
st = "Hello World"
print(st)
print(st.replace('l','z'))

"""
23.split() : split() method is used to split the string into list of substrings.
"""
st = "Hello World"
print(st)
print(st.split())

"""
24.join() : join() method is used to join the list of substring into string.
"""
li = ["welcome","to","my","show"]
print(li)
print(" ".join(li))