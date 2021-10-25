from typing import Counter


inp = input('enter the number of elements : ')
num = int (inp)

prevprev = 0
prev = 1
counter = 0

if num <= 0 :
    print('Please enter a positive number !')
elif num == 1:
    print(prevprev)
else :
    print(prevprev)
    print(prev)
    result = prev + prevprev
    while counter < num-2:
        result = prev + prevprev
        print(result)
        prevprev = prev
        prev = result
        counter += 1