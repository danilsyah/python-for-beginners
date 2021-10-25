<<<<<<< HEAD
inp = input('Enter the string : ')
b = '(){}[]'
final = ''
for c in inp :
    if c not in b :
        final = final + c

print(final)
=======
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulus(x, y):
    return x % y


print('-Calculator-')
print('Choose between the operations: ')
print("1.Addition")
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Modulus')

while True:
    choice = input("Enter your choice (1/2/3/4/5/exit) : ")
    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input('Enter first number : '))
        num2 = float(input('Enter second number : '))

        if choice == '1':
            print(add(num1, num2))
        elif choice == '2':
            print(subtract(num1, num2))
        elif choice == '3':
            print(multiply(num1, num1))
        elif choice == '4':
            print(divide(num1, num2))
        else:
            print(modulus(num1, num2))
    elif choice == 'exit':
        break
    else:
        print('Invalid number!')
>>>>>>> 65ffda929cafca174840511ce3551f370332a2ac
