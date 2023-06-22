from random import randint
from string import punctuation
# Some special characters aren't included in punctuation module - so add them as below
punctuation = punctuation + '£'

initial_input = input("Please type in a string. ")
# Records the indexes of the upper case letters
upper_case_idx = [idx for idx, item in enumerate(initial_input) if ord(item)>=65 and ord(item)<=90]
user_input = initial_input.lower()
key_randint = []
encrypted = []

# Lowercase ascii runs from 97 - 122
for letter in user_input:
    # If the element in the list is a letter of the alphabet increase the ord value by 1-26 and store the randint values in key_randint
    if not(letter == ' ' or letter in punctuation or letter.isdigit()):
        single_key_value = randint(1, 26)
        key_randint.append(single_key_value)
        result = ord(letter) + single_key_value
        # If the ord value is above the ascii range for lowercase letters loop back round from ascii "a"(97)
        if result > 122:
            result = 97 + (result-(123))
        encrypted.append(chr(result))
    # If element not an alphabet letter append to results list
    if letter == ' ' or letter in punctuation or letter.isdigit():
        encrypted.append(letter)

print(f"Encryption for '{initial_input}' is:\n '{''.join(encrypted)}'")
user_response = int(input("Press 1 to see de-encryption. "))

def de_encryption(encrypted):
    encrypted_chars = []
    # Count provides index value for key_randint in for loop
    count = 0
    for idx, letter in enumerate(encrypted):
        # If the element in the list is a letter of the alphabet reduce the ord value by the randint value it was originally increased by - stored in key_randint
        if not(letter == ' ' or letter in punctuation or letter.isdigit()):
            enc_chr = ord(letter) - key_randint[count]
            # If the ord value is below the ascii range for lowercase letters loop back into ascii range 97-122 by adding 26
            if enc_chr < 97:
                enc_chr += 26
            # Return uppercase letters using the original indexes stored in the global variable, upper_case_idx
            if idx in upper_case_idx:
                encrypted_chars.append(chr(enc_chr).upper())
            else:
                encrypted_chars.append(chr(enc_chr))
            # Increment count for next letter enc_chr calculation
            count += 1
        # If element not an alphabet letter append to results list
        else:
            encrypted_chars.append(letter)

    print(f"Decryption of '{''.join(encrypted)}' using key {key_randint} is:\n '{''.join(encrypted_chars)}'")

if user_response == 1:
    de_encryption(encrypted)
