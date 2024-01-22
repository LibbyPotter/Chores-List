#Libby Potter and Cecile
#1/11/24
#To-Do List

#Initialize
list = ["clean room", " do homework", " wash dishes", " do laundrey", " walk dog"]

#Functions
def add():
    task = input("What do you want to add to your list? ")
    position = int(input("Where would you like to add to your list? "))
    position = position - 1
    list.insert(position, task)
    ToDo()
def view():
    print(list)
    ToDo()
def complete():
    position = int(input("What number item have you completed? "))
    task = input("What task have you comlpleted? ")
    position = position - 1
    list.pop(position)
    list.insert(position, " [x] " + task)
    ToDo()
def remove():
    position = int(input("Where would you like to remove from your list? "))
    list.pop(position)
    ToDo()
def exit():
    print("Shutting down, have a good day.")
def ToDo():
    print("Welcome to your daily To-Do list!")
    choice = int(input("Please Choose what you want to do. \n 1. Add to list \n 2. View list \n 3. Mark task as completed \n 4. Remove from list \n 5. Exit \n"))
    if choice==1:
        add()
    if choice==2:
          view()
          
    if choice==3:
          complete()
    if choice==4:
          remove()
    if choice==5:
          exit()
   


#Main
ToDo()