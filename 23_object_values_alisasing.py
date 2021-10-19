a = 'hello'
b = 'hello'
print(a is b)

a = [1, 2, 3]
b = list()
b.extend(a)
a[0] = 4
print('a', a)
print('b', b)
print(a is b)
