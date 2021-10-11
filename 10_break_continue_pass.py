while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        # better try again... Return to the start of the loop
        continue
    else:
        # age was successfully parsed!
        # we're ready to exit the loop.
        break
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")


print("-"*50)

x = [1, 2, 4, 3, 5, 2, 1, -2, 3, -5]
for number in x:
    if number < 0:
        print("This list contains at least one negative number !")
        pass
    print(number)
print('done')


# --------------------------------
x = 10
while x > 0:
    if x == 5:
        x -= 1
        continue
    print("Current value of x is : ", x)
    x -= 1

# =-------------------------------------

word = 'danil'
for character in word:
    if character == 'a':
        pass
        print('This is a pass block !, Add something here !')
    print('current letter :', character)
