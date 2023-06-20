# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False
    
    # divisible by 4 and not 100 = true
    # divisible by 400 = true    
    if(year % 4 == 0 and year % 100 != 0):
        leap = True
    elif(year % 400 == 0):
        leap = True
        
    return leap
