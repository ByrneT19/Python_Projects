import random

while True:
    result = []
    dice = int(input('How many dice would you like to roll? Type "0" to exit. '))
    if dice == 0:
        break
    for die in range(dice):
        rolls = random.randint(1, 6)
        print(f'Die {die + 1}: {rolls}')
        result.append(rolls)
    print(f'Your total is {sum(result)}')
