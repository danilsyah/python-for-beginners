dict = {'car': 300, 'tv': 220, 'k': 400}
t = list(dict.items())
print(t)

for key, value in t:
    print(key, value)


l = list()
for key, value in dict.items():
    l.append((value, key))

print(l)
l.sort()
print(l)
