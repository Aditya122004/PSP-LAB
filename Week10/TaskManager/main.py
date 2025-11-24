from TaskManager import TaskManager
tm=TaskManager()
while True:
    ch=0
    print("1.Add Task")
    print("2.Mark Done")
    print("3.Mark Undone")
    print("4.Delete Tasks")
    print("5.Display Tasks")
    print("6.Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        id=input("Enter Task id: ")
        tsk=input("Enter the task: ")
        tm.add_task(id,tsk)
    elif ch==2:
        id=input("Enter Task id: ")
        tm.mark_done(id)
    elif ch==3:
        id=input("Enter Task id: ")
        tm.mark_undone(id)
    elif ch==4:
        id=input("Enter Task id: ")
        tm.delete_task(id)
    elif ch==5:
        print(tm.list_tasks())
    elif ch==6:
        print("Exiting Program")
        break
    else:
        print("Invalid Choice")
