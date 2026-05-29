import re 

def main():
    user_email = input("Enter your email: ").strip()
    email_validator(user_email)


def email_validator(email):
    if re.fullmatch(r"\w+@(\w+\.)?\w+\.\w{3}", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()