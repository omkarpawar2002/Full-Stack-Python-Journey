"""

Mini Project: Student Record Dictionary
Objective

Create a program that stores and manages student information using a dictionary.

"""

students_records = {}

while True:
    choice = int(input("***ENTER YOUR CHOICE***"\
                       "\n 1.ADD STUDENT "\
                       "\n 2.VIEW STUDENT "\
                       "\n 3.VIEW ALL STUDENTS "\
                       "\n 4.UPDATE STUDENT "\
                       "\n 5.DELETE STUDENT "\
                       "\n 6.EXIT : "))
    if(choice == 1):
        student = {}
        numbers = int(input("Enter how many students you want to add : "))
        print("=======================")
        for num in range(numbers):
            stu_id = int(input("Enter student id : "))
            name = input("Enter your name : ")
            age = int(input("Enter your age : "))
            marks = float(input("Enter your marks : "))
            print("=======================")
            student[stu_id] = {"name":name,"age":age,"marks":marks}
        students_records.update(student)
    elif(choice == 2):
        stu_id = int(input("Enter student id : "))
        if(stu_id in students_records):
            print("=======================")
            print(f"Student Id : {stu_id}")
            for key,value in students_records[stu_id].items():
                print(key,"=",value)
            print("=======================")
        else:
            print("=======================")
            print("Record Not Present In Dictionary")
            print("=======================")
    elif(choice == 3):
        if(students_records):
            print("=======================")
            for stu_id,stu_data in students_records.items():
                print(f"Student Id : {stu_id}")
                for key,value in stu_data.items():
                    print(key,"=",value)
                print("====")
            print("=======================")
        else:
            print("=======================")
            print("Student Records Empty!!")
            print("=======================")
    elif(choice == 4):
        stu_id = int(input("Enter student id : "))
        if(stu_id in students_records):
            print("=======================")
            while True:
                ch = int(input("***UPDATE RECORD***"\
                           "\n 1.NAME "\
                           "\n 2.AGE "\
                           "\n 3.MARKS "\
                           "\n 4.EXIT : "))
                if(ch == 1):
                    updated_name = input("Enter updated name : ")
                    students_records[stu_id]["name"] = updated_name
                    print("=======================")
                    print(f"{updated_name} As A New Name Updated Succesfully!!")
                    print("=======================")
                elif(ch == 2):
                    updated_age = int(input("Enter updated age : "))
                    students_records[stu_id]["age"] = updated_age
                    print("=======================")
                    print(f"{updated_age} As A New Age Updated Succesfully!!")
                    print("=======================")
                elif(ch == 3):
                    updated_marks = float(input("Enter updated marks : "))
                    students_records[stu_id]["marks"] = updated_marks
                    print("=======================")
                    print(f"{updated_marks} As A New Marks Updated Succesfully!!")
                    print("=======================")
                elif(ch == 4):
                    print("=======================")
                    print("Successfully Done Update Operation!!")
                    print("=======================")
                    break
                else:
                    print("=======================")
                    print("Incorrect Choice While Updating!!")
                    print("=======================")
            print("=======================")
        else:
            print("=======================")
            print("Record Not Present For Updating!!")
            print("=======================")
    elif(choice == 5):
        stu_id = int(input("Enter student id : "))
        if(stu_id in students_records):
            print("=======================")
            while True:
                ch = int(input("***DELETE RECORD***"\
                           "\n 1.NAME "\
                           "\n 2.AGE "\
                           "\n 3.MARKS "\
                           "\n 4.EXIT : "))
                if(ch == 1):
                    delted_name = students_records[stu_id].pop("name")
                    print("=======================")
                    print(f"{delted_name} As A Name Deleted Succesfully!!")
                    print("=======================")
                elif(ch == 2):
                    deleted_age = students_records[stu_id].pop("age")
                    print("=======================")
                    print(f"{deleted_age} As A Age Deleted Succesfully!!")
                    print("=======================")
                elif(ch == 3):
                    deleted_marks = students_records[stu_id].pop("marks")
                    print("=======================")
                    print(f"{deleted_marks} As A Marks Deleted Succesfully!!")
                    print("=======================")
                elif(ch == 4):
                    print("=======================")
                    print("Successfully Done Delete Operation!!")
                    print("=======================")
                    break
                else:
                    print("=======================")
                    print("Incorrect Choice While Updating!!")
                    print("=======================")
            print("=======================")
        else:
            print("=======================")
            print("Record Not Present For Deletion!!")
            print("=======================")
    elif(choice == 6):
        print("=======================")
        print("Succesfully Exits!!")
        print("=======================")
        break
    else:
        print("=======================")
        print("Incorrect Choice!!") 
        print("=======================")