# jika file tidak dikenal maka error
# f = open('myFile2.txt', 'rt')

# jika file tidak ditemukan maka akan dibuatkan file baru
# f = open('myFile2.txt', 'x')

# jika file tidak exist maka di buatkan file baru
# f = open('myFile3.txt', 'a')

# f = open('myFile4.txt', 'w')

# f = open('myFile.txt')
# count = 0
# for line in f:
#     count += 1
#     print(line)

# print(f'Number of lines is : {count}')

# print('-'*50)

# st = f.read()
# st = f.read(15)
# print(st)

# f = open("myFile.txt")
# st = f.readline()
# print(st)

# f = open("myFile.txt")
# count = 0
# for line in f:
#     if line.startswith("Hai"):
#         print(line)
#         count += 1
# print(f"Count is : {count}")

# f = open("myFile.txt")
# count = 0
# for line in f:
#     line = line.rstrip()
#     if line.find('@gmail.com') != -1:
#         print(line)
#         count += 1
# print('count is :', count)


fileName = input('Please enter a file name :')
try:
    f = open(fileName)
except:
    print('error!')
    fileName = input("Please enter another name : ")

f = open(fileName)
count = 0
for line in f:
    print(line.rstrip())
    count += 1
    print('Count ', count)
f.close()
