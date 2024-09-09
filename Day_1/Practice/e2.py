# Write a program that takes the user’s name as input and greets them with “Hello, [name]!” (replace [name] with the actual input).
# Extend the program to ask for the user’s birth year. Calculate their age and print it.

user_name = input("Enter your name: ")
current_year = 2024
user_birth_year = int(input("Enter your birth year: "))
age = current_year - user_birth_year

print("Hello,", user_name)
print("Your age is", age)