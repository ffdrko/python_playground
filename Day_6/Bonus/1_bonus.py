content = ["All carrots are to be sliced longitudinally", "The carrots were reportedly sliced.", "The slicing was well presented."]

filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for c, i in zip(content, filenames):
    file = open(f"another_file/{i}", "w")
    file.write(c)
    file.close()
