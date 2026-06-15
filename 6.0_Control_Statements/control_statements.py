# Control Statements 
'''
Control Statements are used when we want to execute certain code statements in a repetative manner.

There are 2 types of control statements :
    1.For loop
    2.While loop

There are 3 types of loop control statements :
    1.break
    2.continue
    3.pass
'''

# range(start,stop,step) :
'''
1.range() function is used to generate sequence of number.
2.It take 3 arguments start , stop , step .
3.start and step both are optional means if we not defined then it start from 0 and step is 1.
4.But mandatory provide stop value.
''' 
for i in range(1,11,1):
    print(i)


# for loop :
'''
1.when we know exact number of time iteration is required then we used for loop.
2.For loop also iterate over sequences like list,tuple,string and also work with range() function.
3.We can also iterate for loop over set and dictionary.
'''
li = [10,20,30,40,50]
for i in li:
    print(i)

name = "krishna"
for i in name:
    print(i)

user = {
    'name':'user_1',
    'password':'user@123'
}
for i in user:
    print(i,"--",user[i])


# while loop :
'''
When we don't know exact number of time the iteration is required then we used while loop.
The loop keep running until the specify condition is True.
'''
i = 1
while i < 5:
    print(i)
    i += 1


# break :
'''
break keyword is used when we immediately wants to exits from the loop.
'''
for i in range(1,11):
    if(i == 4):
        break
    print(i)


# continue :
'''
Continue keyword is used when we want to skip the current iteration and jump on the next iteration.
'''
for i in range(1,6):
    if(i == 4):
        continue
    print(i)


# pass :
'''
pass keyword is used when our program is syntactically correct but we don't want to implement or not do anything in block so we used pass.
'''
for i in range(1,11):
    pass


# nested loop :
'''
When loop inside another loop known as a nested loop in python.
'''
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()