a = ['a', 'b', 'c']
b = [1, 2, 3, 4]
# menggabungkan list a dan b
a.extend(b)
print(a)

c = [2, 5, 7, 4, 9, 3, 1]
c.sort()
print(c)

d = ['danil', 'haykal', 'alin', 'razil', 'fika']
d.sort(reverse=True)
print(d)

print(len(c))
print(max(c))
print(min(c))
print(sum(c)/len(c))

print("-"*50)

total = 0
counter = 0
while True:
    inp = input("Please enter a number : (Done if finished) : ")
    if inp.lower() == 'done':
        break

    number = float(inp)
    total += number
    counter += 1

avg = total / counter
print(f'Average : {avg}')

print("-"*50)

list1 = list()
while True:
    inp = input('Enter a number : ')
    if inp == 'done':
        break
    number = float(inp)
    list1.append(number)

average = sum(list1)/len(list1)
print(average)
