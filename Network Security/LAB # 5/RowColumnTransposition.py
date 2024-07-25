def keyword_num_assign(key):
    """ Assign numbers to keywords based on their alphabetical order """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicate characters
    kywrd_num_list = [0] * len(key)

    for i, char in enumerate(key):
        kywrd_num_list[i] = sorted(key).index(char) + 1

    return kywrd_num_list


def get_number_location(key, kywrd_num_list):
    """ Get column locations based on sorted keyword numbers """
    num_loc = ""
    sorted_indices = sorted(range(len(key)), key=lambda k: kywrd_num_list[k])

    for index in sorted_indices:
        num_loc += str(index)

    return num_loc


def cipher_encryption():
    """ Encrypt the plaintext using Columnar Transposition Cipher """
    msg = input("Enter Plain Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    kywrd_num_list = keyword_num_assign(key)

    # Print keyword and its numeric assignments
    print("Keyword:", key)
    print("Keyword Numeric Assignments:", kywrd_num_list)
    print("-------------------------")

    # Padding message to fit the grid
    extra_letters = len(msg) % len(key)
    if extra_letters != 0:
        msg += "." * (len(key) - extra_letters)

    num_of_rows = len(msg) // len(key)

    # Creating grid
    arr = [list(msg[i * len(key):(i + 1) * len(key)]) for i in range(num_of_rows)]

    # Printing grid
    for row in arr:
        print(' '.join(row))

    num_loc = get_number_location(key, kywrd_num_list)

    # Encryption
    cipher_text = ""
    for i in num_loc:
        cipher_text += ''.join(row[int(i)] for row in arr)

    print("Cipher Text:", cipher_text)


def cipher_decryption():
    """ Decrypt the ciphertext using Columnar Transposition Cipher """
    msg = input("Enter Cipher Text: ").replace(" ", "").upper()
    key = input("Enter keyword: ").upper()

    kywrd_num_list = keyword_num_assign(key)
    num_of_rows = len(msg) // len(key)

    num_loc = get_number_location(key, kywrd_num_list)

    # Creating grid
    arr = [[''] * len(key) for _ in range(num_of_rows)]

    # Decryption
    idx = 0
    for i in num_loc:
        for row in range(num_of_rows):
            arr[row][int(i)] = msg[idx]
            idx += 1

    # Convert grid to plaintext
    plain_text = ''.join(''.join(row) for row in arr).rstrip('.')

    print("Plain Text:", plain_text)


# Main

choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
if choice == 1:
    print("Encryption")
    cipher_encryption()
elif choice == 2:
    print("Decryption")
    cipher_decryption()
else:
    print("Invalid Choice")
