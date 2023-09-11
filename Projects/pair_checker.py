paired_list = [1,2,1,4,2,4,7,8,9,8,9]
s = set()
for ele in paired_list:
    s.add(ele) if ele not in s else s.remove(ele)
print(f'The unpaired number is: {list(s)[0]}')