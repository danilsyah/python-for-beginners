student = {
    'name': 'danil',
    'age': 27,
    'country ': 'Indonesia'
}

print(student)
print(student['name'])

# add element
student['name2'] = 'syah'
print(student)

# remove element
student.pop('name2')
print(student)

student.popitem()
del student['age']
print(student)

# remove all element
student.clear()
print(student)

# mencari jumlah setiap karakter
st = 'Hello my name is danil'
d = dict()
for c in st:
    d[c] = d.get(c, 0) + 1
print(d)
