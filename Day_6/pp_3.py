member = input("Enter the member name: ") + '\n'

file = open('File/members.txt', 'r')
member_list = file.readlines()
file.close()

member_list.append(member)

file = open('File/members.txt', 'w')
file.writelines(member_list)
file.close()