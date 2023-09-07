def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while start < len(line) and line[start].isspace():
                start = start + 1

            if line[start].isdigit():
                end = start
                while end < len(line) and line[end].isdigit():
                    end = end + 1
                words.append(line[start:end])
                start = end

            elif line[start].isalpha():
                end = start
                while end < len(line) and line[end].isalpha():
                    end = end + 1
                words.append(line[start:end].lower())
                start = end


            else:

                words.append(line[start])

                start = start + 1
    return words


print(tokenize(['10. Apple, 10 sweet hello']))
