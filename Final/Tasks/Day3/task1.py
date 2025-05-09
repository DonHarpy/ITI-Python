DataBase = [{"name":"mustafa","password":"123"},{"name":"harpy","password":"456"}]

name = input("Please Enter Your Username: ").strip()

if not name.isalpha():
    print("Please Enter a Valid Username.")
else:
    for i in DataBase:
        if name != i["name"]:
            print("Username not found!")
            break
        elif name == i["name"]:
            password = input("Please Enter Your Password: ")
            if password == i["password"]:
                print(f"Welcome, {name}")
                break
            else:
                print("Wrong password!")
                
        break        