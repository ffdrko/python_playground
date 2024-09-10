prompt = "Enter a password:"
password = input(prompt)

while password != "pass123":
    print("Try again!!!")
    password = input(prompt)


print("You have enter correct password")