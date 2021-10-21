list1 = [1, 1, 2, 2, 2, 3, 4, 5, 3, 6, 3]
# set akan menghapus data yang duplicate
s = set(list1)
print(s)

s1 = set()
s2 = set()

for i in range(10):
    s1.add(i)
    
for i in range(2,16):
    s2.add(i)
    
s2.add(15)
s1.add(15)
# mencocokan data yang sama menggunakan menthod set
print('set 1 : ', s1) 
print('set 2 : ', s2) 
s3 = s1.intersection(s2)
print(s3)

# mencocokan data yang sama menggunakan operasi &
s4 = s1&s2 
print(s4)

# menampilkan data yang berbeda
s5 = s2.difference(s1)
print('data yang tidak sama dari set2 dan set1', s5)

print("-"*50)

l1 = [1,2,3,4,5,6,7]
l2 = [1,5,8,0]
l3 = [1,2,3,7,8,9]

s1=set(l1)
s2=set(l2)
s3=set(l3)
inter = s1.intersection(s2)
print(inter)
interFinal = inter.intersection(s3)
print(interFinal)