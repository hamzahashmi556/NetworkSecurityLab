import random


# generate random key for cipher
def generate_random_key(length):
    return ''.join([chr(random.randint(65, 90)) for i in range(length)])


# plain text to binary conversion
def plaintext_to_binary(pt):
    return [format(ord(char), '08b') for char in pt]


# repeating key to the length of plain text
def repeat_key(key, length):
    repeats = length // len(key)
    remainder = length % len(key)
    return (key * repeats) + key[:remainder]


# key to binary conversion
def key_to_binary(key):
    return [format(ord(char), '08b') for char in key]


# encrypting plaintext using XOR gate
def encrypt(plaintext_binary, key_binary):
    encrypted = []
    for pt, key in zip(plaintext_binary, key_binary):
        encrypted.append(''.join(str(int(pt_bit) ^ int(key_bit)) for pt_bit, key_bit in zip(pt, key)))
    return encrypted


# decrypting cipher text using XOR gate
def decrypt(encrypted_message, key_binary):
    decrypted = []
    for em, key in zip(encrypted_message, key_binary):
        decrypted.append(''.join(str(int(enc_bit) ^ int(key_bit)) for enc_bit, key_bit in zip(em, key)))
    return decrypted


# Function to convert binary to ASCII characters
def binary_to_plaintext(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))


# Decrypting cipher text using XOR gate
def decrypt(encrypted_message, key_binary):
    decrypted = []
    for em, key in zip(encrypted_message, key_binary):
        decrypted.append(''.join(str(int(enc_bit) ^ int(key_bit)) for enc_bit, key_bit in zip(em, key)))
    return decrypted


plaintext = input("Enter the plain text : ").upper()
key_length = len(plaintext)
key = generate_random_key(key_length)
print("Plaintext:", plaintext)
print("Key:", key)
plaintext_binary = plaintext_to_binary(plaintext)
key_repeated = repeat_key(key, key_length)
key_binary = key_to_binary(key_repeated)
print("plain text in binary is : ", plaintext_binary)
print("Binary key", key_binary)
encrypted_message = encrypt(plaintext_binary, key_binary)
print("Encrypted Message (Binary):", encrypted_message)
decryptrd_message = decrypt(encrypted_message, key_binary)
print("Decrypted message(Binary) ", decryptrd_message)
# Decrypt the message
decrypted_binary_message = decrypt(encrypted_message, key_binary)
# Convert decrypted binary message to plaintext
decrypted_plaintext = ''.join(binary_to_plaintext(binary) for binary in decrypted_binary_message)
print("Decrypted message (Plaintext):", decrypted_plaintext)
