input_text = "Please select an operation via it's number (Type 0 to exit programme): \
    \n 1. Addition \n 2. Subraction \n 3. Division \n 4. Remainder \
    \n 5. Multiplication \n 6. Square \n 7. Cube \n 8. Power  \
    \n 9. Factorial \n 10. Absolute Value \n 11. Square Root  \n 12. Cube Root\
    \n 13. Mean Average \n 14. Modal Average \n 15. Median Average \n"

def add():
    user_input = input("Enter values separated by space: ")
    user_input = user_input.split()
    sum = 0
    for n in user_input:
        sum += float(n)
    print(sum)
    #Alternate solution,
    #x = [int(item) for item in x]
    #print(sum(x))

def subtract():
    user_input_one = float(input("Enter your starting value: "))
    user_input_two = float(input("Enter the value to subtract: "))
    result = user_input_one - user_input_two
    print(result)

def divide():
    dividend = float(input("Enter your numerator: "))
    divisor = float(input("Enter your divisor: "))
    try:
        quotient = dividend / divisor
        print(quotient)
    except Exception as e:
        print("There is an error in your input: ", e)
   
def remainder():
    user_input_one = float(input("Enter your numerator: "))
    user_input_two = float(input("Enter your divisor: "))
    result = user_input_one % user_input_two
    print('Remainder is: ', result)
    
def multiply():
    user_input = input("Enter values separated by space: ")
    nums = user_input.split()
    result = 1
    for n in nums:
        result *= float(n)
    print(result)

def square():
    num = float(input("Enter the number you wish to square: "))
    result = num ** 2
    print(result)

def cubed():
    num = float(input("Enter the number you wish to cube: "))
    result = num ** 3
    print(result)

def power():
    num = float(input("Enter the number you wish to raise: "))
    x = float(input("Enter the power to raise it to: "))
    result = num ** x
    print(result)

def fact_num():
    ## Input checks whether user enters a single number
    try:
    	## Input is converted to an integer (so if the user enters more than one number the error will be thrown as there can be no spaces in an int method)
        x = float(input('Enter a single number:'))
        ## If input is fine the recursive function is called
        print(factorial(x))
    except ValueError as e:
    	## If the user enters anything other than a single number this error will be thrown
        print(e, 'Please enter a numercial value.')
        
def factorial(x):
    if x <= -1:
        return ('You cannot use a negative number')
    elif x <= 1:
        return 1
    elif x > 1:
        return factorial(x-1) * x
    
def absolute():
    user_input = float(input("Enter a number: "))
    result = 0
    if user_input < 0:
        result = -1 * user_input
    else:
        result = user_input
    print(result)

def squareRoot():
    user_input = float(input("Enter a number: "))

    result = pow(abs(user_input), 0.5)
    if user_input < 0:
        result = -result
    print(result)

def cubeRoot():
    user_input = float(input("Enter a number: "))

    result = pow(abs(user_input), 1/3)
    if user_input < 0:
        result = -result
    print(result)

def meanAverage():
    user_input = input("Enter numbers seperated by a space: ")
    user_set = user_input.split()
    total = 0
    for n in user_set:
        total += float(n)
    result = total / len(user_set)
    print(result)

def modalAverage():
    user_input = input("Enter numbers seperated by a space: ")
    user_set = user_input.split()
    d = {}    
    for item in user_set:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    max_value = max(v for v in d.values())
    for key, value in d.items():
        if value == max_value:
            print(key)

def medianAverage():
    user_input = input("Enter numbers seperated by a space: ")
    user_set = user_input.split()
    user_set = [float(item) for item in user_set]
    user_set = sorted(user_set)
    result = 0 
    isodd = len(user_set) % 2 != 0
    iseven = len(user_set) % 2 == 0    
    if len(user_set) == 1:
        result = user_set[0]
    if isodd:
        i = int(len(user_set) / 2)
        result = user_set[i]
    if iseven:
        median = int(len(user_set) / 2)
        user_set = [float(n) for n in user_set]
        result = (user_set[median - 1] + user_set[median]) / 2
    print(result)



while True:
    operationInput = int(input(input_text))

    if(operationInput == 0):
        break

    if(operationInput == 1):
        add()
    
    if(operationInput == 2):
        subtract()
    
    if(operationInput == 3):
        divide()

    if(operationInput == 4):
        remainder()
    
    if(operationInput == 5):
        multiply()

    if(operationInput == 6):
        square()
    
    if(operationInput == 7):
        cubed()
    
    if(operationInput == 8):
        power()
    
    if(operationInput == 9):
        fact_num()

    if(operationInput == 10):
        absolute()

    if(operationInput == 11):
        squareRoot()

    if(operationInput == 12):
        cubeRoot()
    
    if(operationInput == 13):
        meanAverage()
    
    if(operationInput == 14):
        modalAverage()

    if(operationInput == 15):
        medianAverage()
