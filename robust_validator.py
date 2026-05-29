from email_validator import validate_email, EmailNotValidError
mail = input("Enter your email: ").strip()
try:
    validate_email(mail)
    print("Valid Email")
except EmailNotValidError:
    print("Invalid Email")