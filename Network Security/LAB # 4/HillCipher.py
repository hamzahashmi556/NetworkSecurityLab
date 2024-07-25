import random

plain_text = str(input("Enter Plain Text: ")).lower()
plain_text = plain_text.replace(" ", "")

print("plain text length", len(plain_text))
pt_break = 0

# Determine block size based on length
block_size = 3
if len(plain_text) % block_size != 0:
    plain_text += 'x' * (block_size - len(plain_text) % block_size)

print("plain text (padded if needed):", plain_text)

# Breaking the string into blocks
blocks = [plain_text[i:i + block_size] for i in range(0, len(plain_text), block_size)]
print("blocks:", blocks)

# Convert blocks to their ASCII values (0-25)
pt_ascii = [[ord(char) - ord('a') for char in block] for block in blocks]
print("ASCII values of blocks:", pt_ascii)

# Generating a random 3x3 key matrix (example used here for simplicity)
key = [[15, 11, 25], [13, 18, 9], [18, 5, 2]]
print("\nKey:")
for row in key:
    print(row)

# Encrypting each block
enc_ans = []
for block in pt_ascii:
    for i in range(block_size):
        enc_value = sum(block[j] * key[j][i] for j in range(block_size)) % 26
        enc_ans.append(enc_value)

print("Encrypted values:", enc_ans)

# Converting encrypted values back to characters
encrypt = [chr(val + ord('a')) for val in enc_ans]
print("Encrypted text:", ''.join(encrypt))
