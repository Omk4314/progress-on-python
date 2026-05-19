import sys

pending_tasks = []
completed_tasks = []


def main():
    print("\n\tWelcome to the app!")
    while True:
        while True:
            usr = input("What would you like to do?(choose the corresponding number)\n1.Add Tasks\n2.Mark complete\n3.View Tasks\n4.Remove Task\n5.Press 'q' to quit\n-> ")
            if usr == "1" or usr == "2" or usr == "3" or usr == "4" or usr == "q":
                break
        match usr:
            case "1":
                add_task()
            case "2":
                mark_complete()
            case "3":
                filters()
            case "4":
                remove_task()
            case "q":
                sys.exit()


#Add
def add_task():
    '''Adds Task to pending_tasks'''
    new_task = input("Enter the new task: ").strip()
    pending_tasks.append(new_task)
    print("Task Added")
    print_tasks(pending_tasks)


#Remove
def remove_task():
    '''Removes the Task mentioned by the user'''
    rmove = input("Enter the task you want to remove: ").strip()
    if rmove in pending_tasks:
        pending_tasks.remove(rmove)
        print_tasks(pending_tasks)
    elif rmove in completed_tasks:
        completed_tasks.remove(rmove)
        print_tasks(completed_tasks)
    else:
        print("Task not found!")


#Mark Complete
def mark_complete():
    '''Transfers the task completed by the user from pending_tasks to completed_tasks'''
    complete = input("Enter the task you want to mark complete: ").strip()
    if complete in pending_tasks:
        completed_tasks.append(pending_tasks.pop(pending_tasks.index(complete)))
    elif complete in completed_tasks:
        print("Task already completed!")
    else:
        print("Task not Found!")

#Filter by status
def filters():
    '''Let's user filter between pending tasks and completed tasks'''
    filter_task = input("Which tasks do you want to see?(Pending/Completed): ").strip().lower()
    if filter_task == "pending":
        if pending_tasks:
            print_tasks(pending_tasks)
        else:
            print("No Task Found!")
    elif filter_task == "completed":
        if completed_tasks:
            print_tasks(completed_tasks)
        else:
            print("No Task Found!")
    else:
        print("Invalid input!")
    
# print tasks
def print_tasks(t):
    '''prints the list of tasks to the screen'''
    for tsk in t:
        print(tsk)

#calling the main function
main()