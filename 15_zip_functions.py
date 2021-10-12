list1 = ['a', 'b', 'c', 'd']
list2 = ['A', 'B', 'C', 'D', 'E']

ZippedList = list(zip(list1, list2))
print(ZippedList)

a, b = list(zip(*ZippedList))
print(a)
print(b)

for(l1, l2) in zip(list1, list2):
    print(l1)
    print(l2)

listFuits = ['banana', 'apple', 'orange']
count = [3, 4, 5]
price = [5000, 3000, 4000]
sq = []

for (fruit, counter, harga) in zip(listFuits, count, price):
    counter, harga = str(counter), str(harga)
    # print(f"I bought {counter} {fruit}s at Rp. {harga}")
    s = 'I Bought '+counter + " " + fruit + "s at Rp." + harga
    sq.append(s)

print(sq)
