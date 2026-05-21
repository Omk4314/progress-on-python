#building a contact book
# contact -> information = mobile number, email, address
import sys
contacts = {}
app_running = True


def main():
    '''main function'''
    global app_running
    while app_running:
        print("\n\tWELCOME TO CONTACT BOOK\n")
        while True:
            ask_user = input('''What would you like to do?\n
                            (Choose the corresponding number of the task you want to perform)\n
                            1. Add/Save new contact\n
                            2. View contacts\n
                            3. Delete contact\n
                            (press 'q' to quit)\n -> ''').strip().lower()
            if ask_user == "1" or ask_user == "2" or ask_user == "3" or ask_user == "q":
                break

        match ask_user:
            case "1":
                save_contact()
            case "2":
                show_contacts()
            case "3":
                delete_contact()
            case "q":
                sys.exit()


def save_contact():
    '''Saves user's contact'''
    global app_running
    while app_running:
        if not app_running:
            break
        name = input("Enter name: ")
        user = {}
        contacts[name] = user
        while True:
            while True:
                user["mob"] = input("Enter Mobile No.: ").strip()
                user["email"] = input("Enter email: ").strip()
                user["add"] = input("Enter address: ").strip()
                if user["mob"].isdecimal():
                    break
                else:
                    print("Invalid Mobile No.")

                if "@" in user["email"]:
                    break
                else:
                    print("Invalid email!")
                
            print("Contact saved...\n")
            show_contacts()
            break
        while True:
            response = input("Do you want to save another contact?(yes/no)? ")
            if response == "yes" or respone == "no":
                break
        if response == "no":
           app_running = False


def show_contacts():
    '''Shows contact's of the user'''
    if contacts:
        print_contact()
    else:
        print("No Contacts found!")

def delete_contact():
    '''Deletes a contact'''
    show_contacts()
    delete = input("Enter the name of the you want to delete: ")
    if delete in contacts:
        del contacts[delete]
    else:
        print("No contact found!")


def print_contact():
    '''prints contacts'''
    for contact, user_info in contacts.items():
        print(f"Contact name: {contact}\nPhone No.: {user_info["mob"]}\nEmail: {user_info["email"]}\nAddress: {user_info["add"]}\n")


#Calling the main function
main()