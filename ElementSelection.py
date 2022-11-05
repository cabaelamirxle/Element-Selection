from array import *
def mainMenu():
    print("1. Add an element")
    print("2. Insert an element")
    print("3. Arrange in ascending order")
    print("4. Arrange in descending order")
    print("5. Count all elements")
    print("6. Sum all elements")
    print("")
    
    selection = int(input("What do you want to do? (1-6): "))
    if selection==1:
        add()
    elif selection==2:
        insert()
    elif selection==3:
        ascending()
    elif selection==4:
        descending()
    elif selection==5:
        count()
    elif selection==6:
        total()
    elif selection==7:
        exit
    else:
        print("")
        print("Invalid choice. Enter 1-6 ")
        print("")
        
def add():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    x=int(input("Enter the number you want to add: "))
    index.append(x)
    print (index)
    print("The number added successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
    
def insert():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    num_ins = int(input("Enter the number you want to insert: "))
    place_ins = int(input("Where do you want to put it: (0-9) "))
    index.insert(place_ins, num_ins)
    print(index)
    print("The number inserted successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
    
def ascending():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    print("this are the current arrangement: [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]")
    anykey = input("enter anything to arange the index from lowest to highest ")
    index.sort()
    print(index)
    print("Index sorted from lowest to highest successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
    
def descending():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    print("this are the current arrangement: [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]")
    anykey = input("enter anything to arange the index from highest to lowest ")
    index.reverse()
    print(index)
    print("Index sorted from highest to lowest successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
    
def count():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    print("this are the index: [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]")
    anykey = input("enter anything to count the index ")
    print(len(index))
    print("The index counted successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
    
def total():
    index = [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]
    print("this are the index: [2, 1, 4, 3, 6, 5, 8, 7, 0, 9]")
    anykey = input("enter anything to sum all the index ")
    total = sum(index)
    print(total)
    print("The total of the index calculated successfully!")
    anykey = input("enter anything to go back")
    mainMenu()
        
mainMenu()