filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentation.txt"]

for file in filenames:
    print(file.replace('.', '-', 1))