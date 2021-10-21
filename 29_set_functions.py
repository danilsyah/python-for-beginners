st = input('Enter a string : ')
vowel = set('aeiouAEIOU')
count = 0

# mencetak jumlah huru vokal yang d input
for c in st:
    if c in vowel:
        count += 1
print('Nb of vowels : ', count)