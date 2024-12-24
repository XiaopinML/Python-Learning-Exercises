# an app that checks if user input is odd or even 
# asks the user to input a number (an integer)
while True:
    try:
        numb = int(input('Please enter a number\n'))
        break
    except ValueError:
        print('Please input an integer number only')

if numb % 2 == 0:
    print('This is an even number')
else:
    print('This is an odd number')
if numb % 4 == 0:
    print('This number is multiple of 4 ')
else:
    print('This number is not multiple of 4')