inp = input('Enter the first number : ')
num = int(inp)
factorial = 1
if num < 0 :
    print("factorial doesn't exist!")
elif num == 0:
    print('the factorial of 0 is 1')
else :
    for i in range(1, num +1 ):
        factorial = factorial * i
    print(f'the factorial of {num} is {factorial} !')
    
