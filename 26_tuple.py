t = ('1', '2', '3', '4', '2', '2')
print(t)


print(t.index('3'))
print(t.count('2'))

# update element
t = ('5',)+t[1:]
print(t)
t = ('6',)+t[1:]
print(t)

st = 'danil.syah'
x, y = st.split('.')
print(x)
print(y)

t1 = (1, 2, 100, 10000, 100000)
t2 = (1, 4, 100)
print(t1 > t2)
