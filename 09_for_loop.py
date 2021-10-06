"""belajar looping"""

name = "danil"

for i, x in enumerate(name):
    print("index ke-",i, " = ",x)
    
for x in range(10):
    print(x)

print("-" * 50)
 
for x in range(5, 10):
    print(x)
    
x = "Hello"
y = "World"
for hello in x :
    for world in y :
        print(hello, world)

print("-" * 50)
        
a = 5
b = 5
for i in range(a):
    for j in range(b):
        print(i, j)
        

print("-"*50)
# menghitung jumlah karakter yang ditentukan
x = "kskadlkalasklfaklwlwkwkkalakfikjkga"
count = 0
for character in x :
    if character is 'a':
        count += 1
print("Count", count)

print("-"*50)

# mencari nilai terbesar
max = 0
x = [1,44,23,56,55,19]
for nb in x :
    if nb > max :
        max = nb
print("nilai max ", max)

# mencari nilai terkecil
x = [4,31,5,312,4, 7, 6]
min = x[0]
for nb in x : 
    if nb < min:
        min = nb
print("nilai terkecil : ", min)