filenames = ['a.txt', 'b.txt', 'c.txt']

for i in filenames:
    file = open(f"File/{i}",'r')
    print(file.read())
    file.close()