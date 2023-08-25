def gapper(binary_number):
    binary = bin(input_num).replace('0b', '')
    binary_number = [int(i) for i in str(binary)]
    indexes = []
    results = []
    print(f'The binary form of this number is: {binary}')
    
    # Find the index of each number 1
    for idx, i in enumerate(binary_number):
        if i == 1:
            indexes.append(idx)
    for j in range(1, len(indexes)):
        # Calculate how many zeros based on the difference between each index of 1
        difference = (indexes[j] - indexes[j-1])-1
        if difference > 0:
            results.append(difference)
    if not results:
        gap = 'No binary gaps'
    else:
        gap = f'There are {str(len(results))} binary gaps, the largest is: {str(max(results))}'
    print(gap)

while True:
    input_num = input('Enter a whole number, enter "0" to exit: ')
    
    if input_num.isdigit():
        if input_num == "0":
            break
        else:
            input_num = int(input_num)
            gapper(input_num)
    else:
        print('Please enter a whole number')
