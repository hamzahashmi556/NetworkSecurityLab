def generate_key(plaintext, key):
    key = list(key)
    if len(plaintext) == len(key):
        return "".join(key)
    else:
        for i in range(len(plaintext) - len(key)):
            key.append(key[i % len(key)])
        return "".join(key)


def encrypt_vigenere(plaintext, key):
    key = generate_key(plaintext, key)
    ciphertext = []
    for i in range(len(plaintext)):
        # Convert character to 0-25 range and apply key
        x = (ord(plaintext[i]) + ord(key[i])) % 26
        # Convert back to ASCII
        x += ord("A")
        ciphertext.append(chr(x))
    return "".join(ciphertext)


def decrypt_vigenere(ciphertext, key):
    key = generate_key(ciphertext, key)
    plaintext = []
    for i in range(len(ciphertext)):
        # Convert character to 0-25 range and apply key
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        # Convert back to ASCII
        x += ord("A")
        plaintext.append(chr(x))
    return "".join(plaintext)


def sanitize_input(text):
    return "".join(filter(str.isalpha, text)).upper()


# Ask the user for the plaintext and the key
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

# Sanitize inputs to remove spaces and non-alphabetic characters
plaintext = sanitize_input(plaintext)
key = sanitize_input(key)

# Encrypt the plaintext
ciphertext = encrypt_vigenere(plaintext, key)
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_text = decrypt_vigenere(ciphertext, key)
print("Decrypted text:", decrypted_text)