'''
generate random number between 0-1
user guesses
if > < print a statement
if == print correct
ask use rwhen they want to stop
'''
from random import uniform


while True:
    random_num = uniform(0, 1)

    user_num = input('Enter a whole or decimal number between 0 and 1. Type e to exit.')

    if user_num == 'e':
        break

    user_num = float(user_num)

    if user_num == random_num:
        print('You got the correct number!!!')

    if user_num > random_num:
        print('Your number is too big!!!')

    if user_num < random_num:
        print('Your number is too small!!!')

