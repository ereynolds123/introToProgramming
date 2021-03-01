while True:
    password = input("Enter your new password: ")
    while True:
        if len(password) >=7:
            break
        print("Your password must be at least 7 characters.")
        password= input("Enter your new password: ")
    
    secondPassword = input("Enter your password again: ")
    if secondPassword == password:
        break
    

print("Your new password is: ", password)