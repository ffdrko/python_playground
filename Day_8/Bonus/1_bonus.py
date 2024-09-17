input_date = input("Enter the day in d/m/y: ")
input_mode_rate = int(input("How do you rate your mood today from 1 to 10? "))
input_dairy = input("Let your thoughts flow: ")

with open(f'../file/{input_date}.txt', 'w') as file:
    file.write(input_dairy)
