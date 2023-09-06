
def tokenize(lines):
    words = []
    for line in lines:
         start = 0
         while start < len(line):
            print(line[start])
            start = start+1

print(tokenize("I am, cool!"))


