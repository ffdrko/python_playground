filenames = ["1.doc", "1.report", "1.presentation"]

filenames = [item.replace(".", "-") for item in filenames]

print(filenames)