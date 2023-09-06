def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1

            print(line[start])
            start = start + 1
    return words
