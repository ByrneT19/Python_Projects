from random import randint
from math import ceil

rounds = int(input('How many rounds do you want to play the best of? '))
user_score = 0
opponent_score = 0

if rounds %2 == 0:
    num_rounds_to_win = int(rounds/2) + 1
else:
    num_rounds_to_win = ceil(rounds/2)

flag_to_continue = True

while flag_to_continue:
    user_selection = '' 
    opponent_selection = ''

    user_input = int(input('Select an option: 1. Paper, 2. Scissors, 3. Rock \n'))
    opponent_input = randint(1, 3)

    if user_input == 1:
        user_selection = 'Paper'
        print(f'You: {user_selection}')
    if user_input == 2:
        user_selection = 'Scissors'
        print(f'You: {user_selection}')
    if user_input == 3:
        user_selection = 'Rock'
        print(f'You: {user_selection}')
    if user_input < 1 or user_input > 3:
        print('Please select a number between 1 - 3')

    if opponent_input == 1:
        opponent_selection = 'Paper'
        print(f'Opponent: {opponent_selection}')
    if opponent_input == 2:
        opponent_selection = 'Scissors'
        print(f'Opponent: {opponent_selection}')
    if opponent_input == 3:
        opponent_selection = 'Rock'
        print(f'Opponent: {opponent_selection}')
    
    # User picks paper
    if user_input == 1:
        if opponent_input == 2:
            opponent_score += 1
            print(f'{opponent_selection} beats {user_selection}!!!')
        if opponent_input == 3:
            user_score += 1
            print(f'{user_selection} beats {opponent_selection}!!!')

    # User picks scissors
    if user_input == 2:
        if opponent_input == 3:
            opponent_score += 1
            print(f'{opponent_selection} beats {user_selection}!!!')
        if opponent_input == 1:
            user_score += 1
            print(f'{user_selection} beats {opponent_selection}!!!')
       
    # User picks rock
    if user_input == 3:
        if opponent_input == 1:
            opponent_score += 1
            print(f'{opponent_selection} beats {user_selection}!!!')
        if opponent_input == 2:
            user_score += 1
            print(f'{user_selection} beats {opponent_selection}!!!')
            
        
    # If both players pick the same
    if user_input == opponent_input:
        print('Draw!!!')

    print('====>>>> Your Score: ', user_score)
    print('====>>>> Opponent Score: ', opponent_score)
    print()

    if user_score >= num_rounds_to_win:
        print('You win!!!')
        flag_to_continue = False
    elif opponent_score >= num_rounds_to_win:
        print('You lose!!!')
        flag_to_continue = False