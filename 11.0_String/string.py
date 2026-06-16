# String :
"""
1.String is a sequence of characters.
2.Anything which kept together inside single quotes , double quotes or triple quotes will be treated as a string in python.
3.String is immutable in nature.
"""

# How to create a string : 
"""
There are 3 ways to create a string :
    1.By using single quote
    2.By using double quote
    3.By using triple quote
"""

# By using single quote :
city_name = 'mumbai'
print(city_name)

# By using double quote :
city_name = "mumbai"
print(city_name)

# By using triple quote :
city_name = """We live in
Mumbai.
"""
print(city_name)

# String is immutable :
"""
We can not change single character inside string.
We can replace entire string with new string but can not change character.
"""
language = "python"
print(language)
# language[2] = "e"  # Here we get an error

# String allows indexing [both positive and negative] :
"""
It supports both indexing positive and negative.
Negative indexing we needed because sometime we want to access the last character in string.
"""
language = "python"
print(language[0])
print(language[2])
print(language[-1])

# String also supports slicing :
"""
As we know if we want to access single character in string then indexing is best choice.
But if we want to work with more than 1 character then we need to slice the string.
"""
language = "python"
print(language[1:4])
print(language[:5])
print(language[::-1])
print(language[1::2])

# To search characters in string we used membership testing :
language = "Java"
print("p" in language)
print("J" in language)
print("C" not in language)
print("p" not in language)

# Concatenation :
"""
[ + ] Operator is used to concatenate both the strings.
"""
first_name = "Hari"
last_name = "Narayan"
print(first_name + last_name)
print(first_name + ' ' + last_name)

# Repetition :
"""
[ * ] Operator is used to repeat string several times.
"""
first_name = "Krishna"
print(first_name * 3)

# Iterate a string over loop :
language = "Python"
for i in language:
    print(i)

"""
Note : So in short we can say ,
    1.If we want to access single character inside string then we go with Indexing.
    2.If we want to work with more than 1 character but not with entire string then we go with Slicing.
    3.If we want to work with every character in string then by iterating over a loop we can access them.
"""

# Escape Sequence Character :
"""
The Escape Sequence Characters are used to format a string in special way :

Commonly Used Escape Sequence Character Are :
    1.\n for new line
    2.\t for tab
    3.\' for single quote
    4.\" for double quote
    5.\\ for backslash
"""
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\'World")
print("Hello\"World")
print("Hello\\World")

# String Formatting Ways :
"""
There are 3 ways to format strings :
    1.f-strings          =====> Highly Used In Projects
    2.format() methods   =====> Sometimes Used In Project
    3.% formatting       =====> Rarely Used So I Am Not Explaining This Concept.
"""

# 1.f-string :
"""
f-string is most recommended way to format the strings.
By using f-string we can put variable,expression directly inside string.
"""
first_name = "Keshav"
age = 34
print(f"My Name Is {first_name} and My Age Is {age}")

# 2.format() method :
"""
format() method also used sometimes while formatting string.
"""
first_name = "Kirti"
age = 23
print("My Name Is {} and My Age Is {}".format(first_name,age))
