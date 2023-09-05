
# document = ['"Come on you spurs"']
document = "Come on you, Spurs"
def tokenize(words):
   list = []
   new_document = words.split()
  # for line in words:
   #  words.split()
   for x in new_document:
      list.append(x)
   
   return list

print(tokenize(document))



