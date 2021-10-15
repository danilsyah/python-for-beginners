# a = untuk menambahkan data
# w = replace data lama jadi data baru
# x = membuat file baru

f = open("myFile5.txt", 'w')
for i in range(10):
    f.write(f'test{i}@something.com\n')

f.close()
