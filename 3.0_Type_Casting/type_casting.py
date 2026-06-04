# Type Casting : 
'''
Type casting is a process of converting one datatype into another.
There are 2 types of type casting in python :
    1.Implicit type casting
    2.Explicit type casting
'''


# Implicit Type Casting : 
'''
When python automatically convert the one data type into another that is known as implicit type casting.
'''
num1 = 10
num2 = 45.5
print(num1 + num2)


# Explicit Type Casting : 
'''
When programmer convert the one data type into another by using python built-in functions that is known as explicit type casting.
'''
age = "22"
age = int(age) + 1
print(age)


# int() :  
'''
int() function is used to convert the data into integer
'''
num = "22"
print(num,type(num))
num = int(num)
print(num,type(num))

is_student = True
print(is_student,type(is_student))
is_student = int(is_student)
print(is_student,type(is_student))

value = 34.5  # Here decimal part will be truncated
print(value,type(value))
value = int(value)
print(value,type(value))


# float() :
'''
float() function is used to convert data into floating point value.
'''
number = 34
print(number,type(number))
number = float(number)
print(number,type(number))

is_student = True
print(is_student,type(is_student))
is_student = float(is_student)
print(is_student,type(is_student))


# str() :
'''
str() function is used to convert data into string.
'''
number = 22
print(number,type(number))
number = str(number)
print(number,type(number))

is_student = True
print(is_student,type(is_student))
is_student = str(is_student)
print(is_student,type(is_student))

number = 45.23
print(number,type(number))
number = str(number)
print(number,type(number))


# bool() :
'''
bool() function is used to convert the data into boolean type.
'''
number = 22
print(number,type(number))
number = bool(number)
print(number,type(number))

num = "34"
print(num,type(num))
num = bool(num)
print(num,type(num))

num = ""
print(num,type(num))
num = bool(num)
print(num,type(num))


# input() :
'''
input() function is used to take input from user.
By default input() function always return in string format.
'''
age = input("Enter your age : ")
print(age,type(age))


# converting input into different data types :
age = int(input("Enter your age : "))
print(age,type(age))


# Taking multiple input
name = input("Enter your name : ")
city = input("Enter your city : ")
print(name)
print(city)


# print()
'''
print() function is used to display the output on screen
'''
print(20+20)


# seperator parameter
'''
By default multiple objects seperated by space but we can seperate them by using sep parameter inside print() function
'''
country = input("Enter country name : ")
state = input("Enter state name : ")
print(country)
print(state)
print(country,state,sep=' ')
print(country,state,sep='-')


# end parameter
'''
By default print the object in next line but we can print on same line also by using end parameter.
'''
country = input("Enter country name : ")
state = input("Enter state name : ")
print(country,end=' ')
print(state)