inp = input('Enter the string : ')
b = '(){}[]'
final = ''
for c in inp :
    if c not in b :
        final = final + c

print(final)