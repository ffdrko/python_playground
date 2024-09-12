files_name = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt")

for file in files_name:
    print(file.replace('.', '-', 1))

print(files_name)
print(type(files_name))