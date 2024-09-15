user_num = int(input("Enter a number: "))

if user_num % 2 == 1:
    print("Weird")
if 2 <= user_num <= 5:
    print("Not Weird")
if 6 <= user_num <= 20:
    print("Weird")
if user_num % 2 == 0 and user_num > 20:
    print("Not Weird")
else:
    print("Weird")