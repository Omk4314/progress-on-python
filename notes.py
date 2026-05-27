import sys
import os

def main():
    print("\tWelcome to notes\n")
    while True:
        print("What would you like to do?")
        while True:
            user_response = input("1.Add a new note\n2.view a note\n3.update a note\n4.Delete a note\n Press 'q' to quit\n-> ")
            if user_response in ("1", "2", "3", "4", "q"):
                break
        match user_response:
            case "1":
                add_note()
            case "2":
                if read_notes().strip() == "":
                    print("No note found, try adding a note first!")
                else:
                    view_note()
            case "3":
                if read_notes().strip() == "":
                    print("No note found, try adding a note first!")
                else:
                    update_note()
            case "4":
                if read_notes().strip() == "":
                    print("No note found, try adding a note first!")
                else:
                    delete_note()
            case "q":
                sys.exit()


def add_note():
    '''Creates a new txt file and asks user for title as the name of file and content of the file'''
    usr_title = input("Enter title: ").strip().title()
    if usr_title in read_notes():
        print("File Already exists")
    else:
        store_notes(usr_title)
        usr_content = input("Write here:\n")
        with open(f"{usr_title}.txt", "w") as file:
            file.write(usr_content)
            print("Saved")
        print(read_notes())

def view_note():
    '''Displays existing notes to the user and asks the user to select a note to read'''
    print(read_notes())
    usr_note = input("Enter the name of the note you want to view: ").strip().title()
    if usr_note in read_notes():
        with open(f"{usr_note}.txt") as file:
            print(file.read())
    else:
        print("Note not found!")


def update_note():
    '''Displays the saved notes to the user and asks user for the file and the content to update'''
    print(read_notes())
    select_note = input("Enter the name of the note you want to update: ").strip().title()
    if select_note in read_notes():
    
        with open(f"{select_note}.txt") as f_ile:
            print(f_ile.read())
        new_content = input("Write new text here:\n")    
        with open(f"{select_note}.txt", "a") as file:
            file.write(f"\n{new_content}")
            print("saved")
        with open(f"{select_note}.txt") as f:
            print(f.read())
    else:
        print("Note not found!")


def delete_note():
    '''Displays notes to the user and asks him to enter the name of a note user wants to delete'''
    print(read_notes())
    del_note = input("Enter the name of the note you want to delete: ").strip().title()
    if del_note in read_notes():
       os.remove(f"{del_note}.txt")
    else:
        print("Note not found!")


def store_notes(note):
    '''Stores the title of the note provided by the user to keep track of notes'''
    with open("notes.txt", "a") as app_file:
        app_file.write(f"{note}\n")


def read_notes():
    with open("notes.txt") as app_file:
        return app_file.read()

if __name__ == "__main__":
    main()