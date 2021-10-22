inp = input('Enter the string : ')
words = inp.split()
words.sort()
print(words, type(words))
delimiter = ' '
inp = delimiter.join(words)
print(inp)
