def emailValidation(email):
    if '@' in email and '.' in email:
        username = email.split("@")[0]
        domain=email.split("@")[1]
        if username.isalnum() and domain:
            domain1= email.split("@")[1].split(".")[0]
            domain2= email.split("@")[1].split(".")[1]
            if domain1 and domain2:
                return f"{email} Is a valid email"
    else:
        return f"{email} Is not a valid email"

Email = input("Enter your Email: ")

print(emailValidation(Email))