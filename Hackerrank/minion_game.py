# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    vowels = 'aeiouAEIOU'
    kevList = 0
    stuList = 0    
    
    for letter in range(len(string)):
        # loops thru the string and checks if the indexed letter is a vowel or not
        # it then takes the length of the string from that letter to the end of the string and adds that number to each player's score
        if string[letter] in vowels:
            # length of string minus the value of the current index to get substring length
            kevList += len(string) - letter
        else:
            # length of string minus the value of the current index to get substring length
            stuList += len(string) - letter

    if stuList > kevList:
        print("Stuart", stuList, end=" ")
    elif kevList > stuList:
        print("Kevin", kevList, end=" ")
    elif stuList == kevList:
        print("Draw")