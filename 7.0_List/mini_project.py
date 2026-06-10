"""

Mini Project – Shopping List Manager
Requirements
Create empty shopping list.
Show menu:
1. Add Item
2. Remove Item
3. View List
4. Exit

Use:
Lists
Loops
Conditions
List Methods

"""

shopping_list = []
while True:
    choice = int(input("***ENTER YOUR CHOICE***"\
                       "\n 1.ADD ITEM "\
                       "\n 2.REMOVE ITEM "\
                       "\n 3.VIEW LIST "\
                       "\n 4.EXIT : "))
    if(choice == 1):
        num = int(input("Enter how many items you want to add : "))
        for i in range(num):
            name = input("Enter item name : ")
            shopping_list.append(name)
    elif(choice == 2):
        item_name = input("Enter item you want to remove : ")
        if(item_name in shopping_list):
            shopping_list.remove(item_name)
        else:
            print("==============================")
            print("Item not present in list")
            print("==============================")
    elif(choice == 3):
        print("==============================")
        print("Here is your item list : ")
        print(shopping_list)
        print("==============================")
    elif(choice == 4):
        print("==============================")
        print("Thank you for shopping")
        print("==============================")
        break
    else:
        print("==============================")
        print("Incorrect Choice!!")
        print("==============================")