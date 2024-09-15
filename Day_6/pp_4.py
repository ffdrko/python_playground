filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    file = open(f'File/{i}', 'w')
    file.writelines("Hello")
    file.close()