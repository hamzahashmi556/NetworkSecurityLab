from typing import List

# Define tables
ip_table = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
            62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
            57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
            61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

pc1_table = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2,
             59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39,
             31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37,
             29, 21, 13, 5, 28, 20, 12, 4]

shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

pc2_table = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
             26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
             51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

e_box_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13,
               12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23,
               24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

s_boxes = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 2, 9, 5, 6, 10, 15, 3, 14, 7, 0, 8],
     [6, 11, 13, 3, 8, 12, 5, 9, 1, 14, 10, 7, 0, 15, 4, 2]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 5, 2, 14, 12, 1, 10, 6, 8, 3, 15, 13, 4, 9, 0],
     [2, 1, 14, 7, 4, 10, 8, 13, 6, 12, 11, 9, 5, 0, 15, 3]]
]

p_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
           2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

inverse_ip_table = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
                    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
                    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
                    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# Helper functions

def permute(block: int, table: List[int], num_bits: int) -> int:
    result = 0
    for i, bit in enumerate(table):
        if block & (1 << (num_bits - bit)):
            result |= (1 << (num_bits - i - 1))
    return result

def shift_left(block: int, shifts: int, num_bits: int) -> int:
    return ((block << shifts) | (block >> (num_bits - shifts))) & ((1 << num_bits) - 1)

def xor(block1: int, block2: int, num_bits: int) -> int:
    return block1 ^ block2

def s_box_substitution(block: int) -> int:
    result = 0
    for i in range(8):
        row = ((block >> (42 - 6 * i)) & 0x20) | ((block >> (41 - 6 * i)) & 0x1)
        col = (block >> (41 - 6 * i)) & 0xF
        result |= s_boxes[i][row][col] << (28 - 4 * i)
    return result

def feistel_function(right: int, key: int) -> int:
    expanded_right = permute(right, e_box_table, 32)
    xor_result = xor(expanded_right, key, 48)
    substituted = s_box_substitution(xor_result)
    return permute(substituted, p_table, 32)

# DES Key Scheduling

def generate_subkeys(key: int) -> List[int]:
    key = permute(key, pc1_table, 56)
    left, right = key >> 28, key & 0xFFFFFFF
    subkeys = []
    for shift in shift_schedule:
        left = shift_left(left, shift, 28)
        right = shift_left(right, shift, 28)
        combined = (left << 28) | right
        subkey = permute(combined, pc2_table, 48)
        subkeys.append(subkey)
    return subkeys

# DES Encryption and Decryption

def des_round(left: int, right: int, subkey: int) -> (int, int):
    new_right = left ^ feistel_function(right, subkey)
    return right, new_right

def des_encrypt_block(block: int, key: int) -> int:
    block = permute(block, ip_table, 64)
    left, right = block >> 32, block & 0xFFFFFFFF
    subkeys = generate_subkeys(key)
    for subkey in subkeys:
        left, right = des_round(left, right, subkey)
    final_block = (right << 32) | left
    return permute(final_block, inverse_ip_table, 64)

def des_decrypt_block(block: int, key: int) -> int:
    block = permute(block, ip_table, 64)
    left, right = block >> 32, block & 0xFFFFFFFF
    subkeys = generate_subkeys(key)
    for subkey in reversed(subkeys):
        left, right = des_round(left, right, subkey)
    final_block = (right << 32) | left
    return permute(final_block, inverse_ip_table, 64)


def text_to_block(text: str) -> int:
    return int.from_bytes(text.ljust(8, '\0').encode('utf-8'), 'big')


def block_to_text(block: int) -> str:
    return block.to_bytes(8, 'big').rstrip(b'\0').decode('utf-8')


# # Example key (must be 64 bits / 8 bytes)
# key = 0x0F1571C947D08E9B
# # Get input text from the user
# text = input("Enter text (up to 8 characters): ")
# # Ensure the text is exactly 8 characters long
# if len(text) > 8:
#     print("Error: Text length must be 8 characters or less.")
# else:
#     # Convert text to 64-bit block
#     block = text_to_block(text)
#     # Encrypt and decrypt the block (using previously defined DES functions)
#     encrypted_block = des_encrypt_block(block, key)
#     decrypted_block = des_decrypt_block(encrypted_block, key)
#     # Convert blocks back to text
#     decrypted_text = block_to_text(decrypted_block)
#     print(f'Original Text: {text}')
#     print(f'Encrypted Block (hex): {encrypted_block:016X}')
#     print(f'Decrypted Block (hex): {decrypted_block:016X}')
#     print(f'Decrypted Text: {decrypted_text}')

# Example usage
plaintext = 0x1234567890ABCDEF
key = 0x0F1571C947D08E9B
encrypted = des_encrypt_block(plaintext, key)
# decrypted = des_decrypt_block(encrypted, key)

# print(f'Plaintext: {plaintext:016X}')
# print(f'Encrypted: {encrypted:016X}')
# print(f'Decrypted: {decrypted:016X}')
