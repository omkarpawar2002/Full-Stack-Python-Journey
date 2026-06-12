"""
Methods :
        As we know dictionary is mutable so we can easily modify or update the value of specified key present in dictionary.
        By using the built-in methods provided by python.
"""

"""
1.get() : get() method is used to return the value of the specified key present in dictionary and if the specified key is not present in dictionary then it return None or We can provide a default value also.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.get("age"))
print(student.get("city","Not found"))

"""
2.update() : update() method is used to add multiple key value pairs i.e.,other dictionary to dictioanry.
"""
student = {
    "name":"Vikas",
    "age":23
}
marks = {
    "physics":67,
    "chemistry":78,
    "maths":93
}
student.update(marks)
print(student)

"""
3.keys() : keys() method returns a view object containing all keys present in the dictionary.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.keys())

"""
4.values() : values() method returns a view object containing all values present in the dictionary.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.values())

"""
5.items() : items() method returns a view object containing all (key:value) tuple present in the dictionary.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.items())

"""
6.clear() : clear() method is used to clear all the dictionary.
"""
student = {
    "name":"Vikas",
    "age":23
}
student.clear()
print(student)

"""
7.copy() : copy() method is used to create a shallow copy of dictionary.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student,id(student))
stu_copy = student.copy()
print(stu_copy,id(stu_copy))

"""
8.pop() : pop() method is used to remove the key:value from dictionary and return the value of key.If key not present then it shows an keyError.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.pop("age"))
print(student)

"""
9.popitem() : popitem() method is used to remove and return last inserted key:value tuple pair.
"""
student = {
    "name":"Vikas",
    "age":23
}
student.popitem()
print(student)

"""
10.fromkeys() : fromkeys() method is used to create a dictionary from given sequence of keys and values.
"""
subjects = ["physics","maths","chemistry","biology"]
student_marks = dict.fromkeys(subjects,0)
print(student_marks)

"""
11.setdefault() : setdefault() method is used to add key:value pair if the specified key is not present in dictionary and if it present then it remains unchanged. setdefault() method return the value of the given key.
"""
student = {
    "name":"Vikas",
    "age":23
}
print(student.setdefault("city","pune"))
print(student)