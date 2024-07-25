# Function to convert the string to lowercase
def to_lower_case(text):
    return text.lower()


# Function to remove all spaces in a string
def remove_spaces(text):
    return text.replace(" ", "")


# Function to group 2 elements of a string as a list element
def digraph(text):
    digraph_list = []
    for i in range(0, len(text), 2):
        digraph_list.append(text[i:i + 2])
    return digraph_list


# Function to fill a letter in a string element if two letters in the same string match
def fill_letter(text):
    for i in range(0, len(text) - 1, 2):
        if text[i] == text[i + 1]:
            text = text[:i + 1] + 'x' + text[i + 1:]
    if len(text) % 2 != 0:  # If the length is odd, add 'x' at the end
        text += 'x'
    return text


# Function to generate the 5x5 key square matrix
def generate_key_table(key, alphabet):
    key_letters = []
    for char in key:
        if char not in key_letters:
            key_letters.append(char)
    for char in alphabet:
        if char not in key_letters and char != 'j':
            key_letters.append(char)

    key_matrix = [key_letters[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


# Function to search for a character in the key matrix and return its position
def search(matrix, element):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == element:
                return i, j


# Function to handle encryption when letters are in the same row
def encrypt_row_rule(matrix, row1, col1, row2, col2):
    new_col1 = (col1 + 1) % 5 if col1 != 4 else 0
    new_col2 = (col2 + 1) % 5 if col2 != 4 else 0
    return matrix[row1][new_col1], matrix[row2][new_col2]


# Function to handle encryption when letters are in the same column
def encrypt_column_rule(matrix, row1, col1, row2, col2):
    new_row1 = (row1 + 1) % 5 if row1 != 4 else 0
    new_row2 = (row2 + 1) % 5 if row2 != 4 else 0
    return matrix[new_row1][col1], matrix[new_row2][col2]


# Function to handle encryption when letters form a rectangle in the matrix
def encrypt_rectangle_rule(matrix, row1, col1, row2, col2):
    return matrix[row1][col2], matrix[row2][col1]


# Function to handle decryption when letters are in the same row
def decrypt_row_rule(matrix, row1, col1, row2, col2):
    new_col1 = (col1 - 1) % 5 if col1 != 0 else 4
    new_col2 = (col2 - 1) % 5 if col2 != 0 else 4
    return matrix[row1][new_col1], matrix[row2][new_col2]


# Function to handle decryption when letters are in the same column
def decrypt_column_rule(matrix, row1, col1, row2, col2):
    new_row1 = (row1 - 1) % 5 if row1 != 0 else 4
    new_row2 = (row2 - 1) % 5 if row2 != 0 else 4
    return matrix[new_row1][col1], matrix[new_row2][col2]


# Function to handle decryption when letters form a rectangle in the matrix
def decrypt_rectangle_rule(matrix, row1, col1, row2, col2):
    return matrix[row1][col2], matrix[row2][col1]


# Function to encrypt text using Playfair Cipher
def encrypt_playfair_cipher(matrix, plaintext):
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        row1, col1 = search(matrix, char1)
        row2, col2 = search(matrix, char2)

        if row1 == row2:  # Same row
            new_char1, new_char2 = encrypt_row_rule(matrix, row1, col1, row2, col2)
        elif col1 == col2:  # Same column
            new_char1, new_char2 = encrypt_column_rule(matrix, row1, col1, row2, col2)
        else:  # Forming a rectangle
            new_char1, new_char2 = encrypt_rectangle_rule(matrix, row1, col1, row2, col2)

        ciphertext += new_char1 + new_char2

    return ciphertext


# Function to decrypt text using Playfair Cipher
def decrypt_playfair_cipher(matrix, ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = search(matrix, char1)
        row2, col2 = search(matrix, char2)

        if row1 == row2:  # Same row
            new_char1, new_char2 = decrypt_row_rule(matrix, row1, col1, row2, col2)
        elif col1 == col2:  # Same column
            new_char1, new_char2 = decrypt_column_rule(matrix, row1, col1, row2, col2)
        else:  # Forming a rectangle
            new_char1, new_char2 = decrypt_rectangle_rule(matrix, row1, col1, row2, col2)

        plaintext += new_char1 + new_char2

    return plaintext


# Taking input from the user to select encryption or decryption
while True:
    choice = input("Enter 'E' for Encryption or 'D' for Decryption: ").upper()
    if choice == 'E':
        break
    elif choice == 'D':
        break
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")

# Taking input from the user
if choice == 'E':
    plaintext = input("Enter the plaintext: ")
elif choice == 'D':
    ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

# Preprocess plaintext and key
plaintext = fill_letter(remove_spaces(to_lower_case(plaintext))) if choice == 'E' else ""
key = to_lower_case(key)

# Generate key matrix
key_matrix = generate_key_table(key, 'abcdefghiklmnopqrstuvwxyz')

# Encrypt the plaintext or Decrypt the ciphertext
if choice == 'E':
    ciphertext = encrypt_playfair_cipher(key_matrix, plaintext)
    print("Cipher Text:", ciphertext)
elif choice == 'D':
    plaintext = decrypt_playfair_cipher(key_matrix, ciphertext)
    print("Plain Text:", plaintext)
