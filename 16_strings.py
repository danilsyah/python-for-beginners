x = "Hello, World"
print(x[2:8])
print(x[5:])
print(x[-3:-7])
print(len(x))

firstName = "Danil"
lastName = "Syah"
fullName = firstName+lastName
print(fullName)
print('A' in fullName)

color = "color:black"
print('color' in color)

name = 'haykal'
counter = 0
while counter < len(name):
    i = name[counter]
    print(i)
    counter += 1

print("-"*50)

for i in name:
    print(i)

print("-"*50)

word = input("Enter a word : ")
if word < 'color':
    print(f"{word} is less than color")
elif word > 'color':
    print(f"{word} is greater than color ")
else:
    print("the word is color")
