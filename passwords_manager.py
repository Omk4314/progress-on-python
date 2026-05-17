from pathlib import Path
import json
import sys

global file
global key
key = 9
file = Path("passwords.txt")
usr_data = {}


#Take command from the user
def command():
    while True:
        while True:
            com = input("Enter command(store/retrive/'q' to quit): ").strip().lower()
            if com == "store" or com == "retrive" or com == "q":
                break
            
        if com == "store":
            password_site()
        elif com == "retrive":
            retrive_password()
        else:
            sys.exit()
        
#Store the password
def password_site():
    while True:
        site_name = input("Enter site name: ")
        passwrd = input("Enter password: ")
        usr_data[site_name] = cipher(passwrd, key)
        while True:
            retry = input("Do you want to store a new password(yes/no)? ").lower()
            if retry == "yes" or retry == "no":
                break
        if retry == "no":
            file.write_text(json.dumps(usr_data, indent = 4))
            print("Saved to file..")
            return

#retrive the password
def retrive_password():
    contents = json.loads(file.read_text())
    site = input("Enter site name to retrive your password: ")
    if site in contents:
       usr_password = decrypt(contents[site], key)
       print(f"Your password for {site} is {usr_password}")
    else:
        print(f"Not found site name: {site}")

#Encrypting the password using ceasar cipher
def cipher(strng, k):
    new_strng = ""
    for char in strng:
        if char.isalpha():
            if char.islower():
                c_num = ((ord(char) - ord("a") + k) % 26) + ord("a")
                new_strng += chr(c_num)
            elif char.isupper():
                ch_num = ((ord(char) - ord("A") + k) % 26) + ord("A")
                new_strng += chr(ch_num)
        else:
            new_strng += char
    return new_strng

#Decrypting the password 
def decrypt(pss, k):
    new_pss = ""
    for char in pss:
        if char.isalpha():
            if char.islower():
                char_num = ((ord(char) - ord("a") - k) % 26) + ord("a")
                new_pss += chr(char_num)
            elif char.isupper():
                chr_num = ((ord(char) - ord("A") - k) % 26) + ord("A")
                new_pss += chr(chr_num)
        else:
            new_pss += char
    return new_pss
        
command()