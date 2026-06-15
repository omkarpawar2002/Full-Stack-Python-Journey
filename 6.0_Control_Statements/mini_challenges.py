# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()


# *****
# ****
# ***
# **
# *
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()


# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()


# A
# AB
# ABC
# ABCD
# ABCDE
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()