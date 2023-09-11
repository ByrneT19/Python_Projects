original_list = [1,2,3,4,5]
rotations = 3
rotated_list = [0]*len(original_list)

def rotation(a, k):
    len_a = len(a)
    if len_a == 0: return []
    # If the number of rotations is greater than the length of the list find the remainder based on modulus:
    # I.e. length 6 with rotations == 8 is equal to rotations == 2 as 8 % 6 == 2
    if k > len(a):
        k = k%len_a
    for i in range(len_a):
        if i + k == len_a-1:
            # On left hand-side i + k is the new index, a[i] on right-hand side is the original value at index i
            # a[i] will be assigned to the new index i + k in the resulting rotated list
            rotated_list[i+k] = a[i]
        elif i + k > len_a-1:
            rotated_list[(i+k)-len_a] = a[i]
        else:
            rotated_list[i+k] = a[i]

    print(f'original list {original_list} with {rotations} cycles becomes {rotated_list}')
    return rotated_list

result = rotation(original_list, rotations)
print(result)