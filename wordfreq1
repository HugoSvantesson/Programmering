def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1

            if line[start].isdigit():
                print (line[start]," Is a digit!")
            elif line[start].isalpha():
                print(line[start], " Is a letter!")
            else:
                print(line[start], " Is a symbol!")

            start = start + 1
    return words
