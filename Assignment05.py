# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BGilbertson, 8.4.2021,Added code to add a new task and priority to the list
# BGilbertson, 8.5.2021, Added code to save and exit
# BGilbertson, 8.6.2021, Added code to remove an item from the list
# BGilbertson, 8.7.2021, Cleaned up and commented the code
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = "" # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionary rows
# Initial list of data to a file
objFile = open("ToDoList.txt", "w")
lstRow = ["mop", "l"]
objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
lstRow = ["dust", "l"]
objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
lstRow = ["vacuum", "h"]
objFile.write(lstRow[0] + ',' + lstRow[1] + '\n')
objFile.close()

# Step 1A - Introduce the program, read the initial data from the text file and present it to the user
print(""" \nThis program allows the user to manage  items in a ToDo list 
along with thier priority. You may view, add, or delete ToDo items
and their corresponding priority""")
print("\nThe initial ToDo list contains the following items:")
print("Task  ||  Priority ('l' for low or 'h' for high)\n")
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")  # Returns a list!
    dicRow = {"task": lstRow[0], "priority": lstRow[1].strip()}
    lstTable.append(dicRow)
    print(dicRow["task"] + "  ||   " + dicRow["priority"])
objFile.close()


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task  ||  Priority ('l' for low or 'h' for high)")
        for row in lstTable:
            print(row["task"] + "  ||   " + row["priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("\nEnter a task to do: "))
        strPriority = str(input("Enter its priority 'l' for low, 'h' for high: "))
        if strPriority.lower() == "l" or strPriority.lower() == "h": #checks for a valid priority entry
            dicRow = {"task": strTask,"priority": strPriority}
            lstTable.append(dicRow)
            print("The task: " + strTask + ",  " + "has been added to the list and its priority is:  " + strPriority)
        else:
            print("Please enter only 'l' or 'h' for priority, you are being returned to the main menu")
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        while (True):
            strRemoveTask = input("\nEnter a task to remove or 'exit' to return to the Menu: ")
            if strRemoveTask.lower() == "exit":
                break
            for row in lstTable:
                if row["task"].lower() == strRemoveTask.lower():
                    lstTable.remove(row)
                    print("The row containing  -", strRemoveTask, "-  has been removed")
                    objFile = open("ToDoList.txt", "w") # Open object in write mode
                    for row in lstTable: #This loop will save changes after data removal
                        objFile.write(str(row["task"]) + "," + str(row["priority"]) + "\n")
                    objFile.close()
                    print("\nThe remaining items and their priority in your ToDo list are shown below:")
                    for row in lstTable:
                        print(row["task"] + "  ||   " + row["priority"])
                        continue
                    break
            else:
                print("The item is not in your list")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file.
    elif (strChoice.strip() == '4'):
            objFile = open("ToDoList.txt", "w")
            for row in lstTable:
                objFile.write(str(row["task"]) + "," + str(row["priority"]) + "\n")
            objFile.close()
            print("Your data has been saved")
            continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break
    else: # This code catches incorrect menu choices by the user
       print("Please choose only 1, 2, 3, 4, or 5")

# Display the items in the To Do list for the user and end the program
print("Here is a summary of all the items in your ToDo list.")
for row in lstTable:
    print(row["task"] + "  ||   " + row["priority"])
    continue
print("\nThank you, presss 'enter' to end the program.")
input()