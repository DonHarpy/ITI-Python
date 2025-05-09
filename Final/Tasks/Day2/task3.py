firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
firstName.strip()
lastName.strip()
for i in range(3):
    if not firstName.isalpha():
        print("First name should contain only letters.")
        break
    elif not lastName.isalpha():
        print("Last name should contain only letters.")
fullName = f"{firstName} {lastName}"

email = input("Enter your email address: ")
email.strip()
username = email.split("@")[0]
domain = email.split("@")[1]
splitString = email.split("@")
if username.isalnum() and domain.isalpha() or "@" not in email or "." not in email or splitString[0][-1] != "." and splitString[1][0] != "@":
    print(f"Your Full name is: {fullName}")
    print(f"Your email address is: {email}")
else:
    print("Invalid email address.")

