## LAB # 2

import random

pt = input("Enter the plain text : ")
pt = pt.upper()
# print(pt)
keyword = []

for i in range(random.randint(4, 5)):
    keyword.append(chr(random.randint(65, 90)))
key = ''.join(keyword)



def equalKey(key, pt):
    key_len = len(key)  # length of keyword
    pt_len = len(pt)  # length of plain text
    key_repeat = ''  # repeated keyword
    if key_len == pt_len:
        return key
    elif key_len < pt_len:
        repeat = pt_len // key_len  # need to be repeat the keyword
        reminder = pt_len % key_len  # additional character after repeatition
        key_repeat += key * repeat
        key_repeat += key[:reminder]
        return key_repeat
    elif key_len > pt_len:
        key_repeat += key[:pt_len]
        return key_repeat


def generate_vigenere_table():
    Capital = []  # ascii 65 to 90
    for i in range(26):
        Capital.append([])
        for j in range(26):
            Capital[i].append(chr(((i + j) % 26) + 65))
    for row in Capital:
        print(" ".join(row))
    return Capital


# Generate and print the Vigenère table
vigenere_table = generate_vigenere_table()

repeate_key = equalKey(key, pt)
# print(repeate_key)


# encryption , encryption is done by matrix method
def encrypt(pt, repeate_key, vigenere_table):
    pt = list(pt)
    encrypted = []
    for i in range(len(pt)):
        row = ord(repeate_key[i]) - 65  # Calculate the row index in the Vigenère table
        # print(row)
        col = ord(pt[i]) - 65  # Calculate the column index in the Vigenère table
        # print(col)
        encrypted_char = vigenere_table[row][col]  # Get the character from the Vigenère table
        encrypted.append(encrypted_char)  # Add the encrypted character to the list
    return ''.join(encrypted)


encode = encrypt(pt, repeate_key, vigenere_table)
print('===============')
print(f"Encoded: {encode}")


# decryption, decryption is done by Mod method
def decrypt(encode, vigenere_table, repeate_key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encode = list(encode)
    decrypted = ''
    for i in range(len(encode)):
        result = (ord(encode[i]) - ord(repeate_key[i])) % 26
        decrypted += alphabet[result]
    return decrypted


decode = decrypt(encode, vigenere_table, repeate_key)
print(f"DECODED: {decode}")
print(f"KEY: {key}")