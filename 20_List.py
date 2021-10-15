profil = ["danil", "syah", 27, True, 165.5]
print(profil)

# add element list
profil.append("test")

# update data
profil[0] = "haykal"

# remove
profil.remove("syah")

# pop 
profil.pop(3)

for e,i in enumerate(profil):
    print(e, i)
    

profil[0:2] = ["haykal","tess"]
print(profil)

print("-" * 50)

list2 = [['car',"motocycle", "bike"], 'key', 'tv']
haveKey = 'key' in list2
print(haveKey)

# insert value
list2.insert(2, "dataBaru")
print(list2)
print(list2[0][2])

# delete
del list2[0][1:3]
print(list2)

# pop
list2.pop()
print(list2)

# list clear
list2.clear()
print(list2)

bil = [1,2,3,4,5,6,7,8]

for i,e in enumerate(bil) :
    if i % 2 == 0:
        bil[i] = 'genap'    
print(bil)

bil2 = [1,2,3,4,5,6]

for index in range(len(bil2)):
    bil2[index] *= 2
print(bil2)