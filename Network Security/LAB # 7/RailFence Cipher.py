def encrypt_rail_fence(message: str, key: str) -> str:
    num_rails = int(key)
    if num_rails <= 1:
        return ""

    # Initialize the rail matrix
    rail = [[] for _ in range(num_rails)]

    rail_index = 0
    direction = 1  # 1 for down, -1 for up

    for char in message:
        rail[rail_index].append(char)
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    # Flatten the rail matrix and join the characters
    encrypted_message = ''.join(''.join(row) for row in rail)
    return encrypted_message


def decrypt_rail_fence(cipher_text: str, key: str) -> str:
    num_rails = int(key)
    if num_rails <= 1:
        return ""

    # Determine the length of each rail
    rail_length = [0] * num_rails
    rail_index = 0
    direction = 1

    for _ in range(len(cipher_text)):
        rail_length[rail_index] += 1
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    # Fill the rail matrix with characters from the ciphertext
    rail = [[] for _ in range(num_rails)]
    index = 0
    for i in range(num_rails):
        for _ in range(rail_length[i]):
            rail[i].append(cipher_text[index])
            index += 1

    # Read characters in zigzag manner to decrypt
    result = []
    rail_index = 0
    direction = 1

    for _ in range(len(cipher_text)):
        result.append(rail[rail_index].pop(0))
        rail_index += direction
        if rail_index == 0 or rail_index == num_rails - 1:
            direction *= -1

    return ''.join(result)

# Example usage
message = input("ENTER PLAIN TEXT: ")
key = int(input("ENTER KEY IN NUMBER: "))
while type(key) != int:
    key = int(input("ENTER KEY IN NUMBER: "))
encrypted = encrypt_rail_fence(message, key)
print("Encrypted:", encrypted)

# Example usage
# cipher_text = "HLOLEFIRENCAL"
# key = "3"
decrypted = decrypt_rail_fence(encrypted, key)
print("Decrypted:", decrypted)
