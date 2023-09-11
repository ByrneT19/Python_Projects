paired_list = [1,2,1,4,2,4,8,9,8,9,7]
s = set()
if len(paired_list) % 2 == 0:
    print('There are no unpaired elements.')
else:
    for ele in paired_list:
        s.add(ele) if ele not in s else s.remove(ele)
    print(f'The unpaired number is: {list(s)[0]}')
