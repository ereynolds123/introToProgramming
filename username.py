# Create user name

firstName = input ("Enter first name : ")
lastName = input ("Enter last name: ")

userName = firstName[0] +lastName[:7]
userName= userName.lower()

print("Your username is", userName)