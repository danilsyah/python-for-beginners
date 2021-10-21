School = {
    'class1': {
        'student1': 'Danil',
        'student2': 'Haykal'
    },
    'class2': {
        'student1': 'fika',
        'student2': 'khalinda'
    }
}

print(School)
print(School['class1']['student1'])

names = {
    'haykal': 3,
    'danil': 27,
    'fika': 26
}

list1 = list(names.keys())
list1.sort()
print(list1)

for key in list1:
    print(key, names[key])

for key in names:
    print(key, names[key])
