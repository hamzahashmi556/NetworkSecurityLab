import sympy
from sympy import mod_inverse
import random


# Function to generate a random prime number of a given bit length
def random_prime(bits):
    min_val = 2 ** (bits - 1)
    max_val = 2 ** bits - 1
    while True:
        p = sympy.randprime(min_val, max_val)
        if sympy.isprime(p):
            return p


# Function to generate RSA keys
def generate_rsa_key(keysize):
    e = 65537  # Commonly used prime exponent
    p = q = totient = None

    while True:
        p = random_prime(keysize // 2)
        q = random_prime(keysize // 2)
        totient = (p - 1) * (q - 1)

        if sympy.gcd(e, totient) == 1 and abs(p - q) > 2 ** (keysize // 2 - 100):
            break

    n = p * q
    d = mod_inverse(e, totient)

    return e, n, d


# Function to encode a string to a big integer
def encode_rsa(message):
    encoded_msg = int(''.join(f'{ord(c):02d}' for c in message))
    return encoded_msg


# Function to decode a big integer to a string
def decode_rsa(encoded_msg):
    encoded_str = str(encoded_msg)
    decoded_chars = []
    for i in range(0, len(encoded_str), 2):
        num = int(encoded_str[i:i + 2])
        decoded_chars.append(chr(num))
    return ''.join(decoded_chars).rstrip('\x00')


# Function to encrypt a message
def encrypt_rsa(encoded_msg, n, e):
    return pow(encoded_msg, e, n)


# Function to decrypt a message
def decrypt_rsa(encrypted_msg, d, n):
    return pow(encrypted_msg, d, n)


# Example usage
keysize = 512  # Choose a keysize (e.g., 512 bits)

# Generate RSA keys
e, n, d = generate_rsa_key(keysize)
print(f"Public Key (e, n): ({e}, {n})")
print(f"Private Key (d): {d}")

# Encrypt and decrypt a message
message = input("ENTER PLAIN TEXT: ").upper()
encoded_message = encode_rsa(message)
print(f"Encoded Message: {encoded_message}")

encrypted_message = encrypt_rsa(encoded_message, n, e)
print(f"Encrypted Message: {encrypted_message}")

decrypted_message = decrypt_rsa(encrypted_message, d, n)
decoded_message = decode_rsa(decrypted_message)
print(f"Decoded Message: {decoded_message}")
