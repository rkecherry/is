def prepare_input(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I'
    text = text.replace("J", "I")
    # Split the text into pairs of letters
    pairs = []
    for i in range(0, len(text), 2):
        pair = text[i:i+2]
        if len(pair) == 1:  # If the last pair has only one letter, add 'X' to make it a pair
            pair += 'X'
        pairs.append(pair)
    return pairs

def generate_key_matrix(key):
    # Remove spaces and convert to uppercase
    key = key.replace(" ", "").upper()
    # Replace 'J' with 'I'
    key = key.replace("J", "I")
    # Create a set of unique letters from the key (without duplicates)
    key_set = list(dict.fromkeys(key))
    # Create the key matrix (5x5 grid)
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    i, j = 0, 0
    for letter in key_set:
        key_matrix[i][j] = letter
        j += 1
        if j == 5:
            j = 0
            i += 1
    # Fill the remaining spaces with the remaining letters of the alphabet (excluding 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letter in alphabet:
        if letter not in key_set:
            key_matrix[i][j] = letter
            j += 1
            if j == 5:
                j = 0
                i += 1
    return key_matrix

def find_letter_positions(letter, key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == letter:
                return (i, j)

def encrypt(plaintext, key):
    pairs = prepare_input(plaintext)
    key_matrix = generate_key_matrix(key)
    cipher_text = ''
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_letter_positions(char1, key_matrix)
        row2, col2 = find_letter_positions(char2, key_matrix)
        if row1 == row2:  # Same row
            cipher_text += key_matrix[row1][(col1 + 1) % 5]
            cipher_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            cipher_text += key_matrix[(row1 + 1) % 5][col1]
            cipher_text += key_matrix[(row2 + 1) % 5][col2]
        else:  # Forming rectangle
            cipher_text += key_matrix[row1][col2]
            cipher_text += key_matrix[row2][col1]
    return cipher_text

def decrypt(ciphertext, key):
    pairs = prepare_input(ciphertext)
    key_matrix = generate_key_matrix(key)
    plain_text = ''
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = find_letter_positions(char1, key_matrix)
        row2, col2 = find_letter_positions(char2, key_matrix)
        if row1 == row2:  # Same row
            plain_text += key_matrix[row1][(col1 - 1) % 5]
            plain_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plain_text += key_matrix[(row1 - 1) % 5][col1]
            plain_text += key_matrix[(row2 - 1) % 5][col2]
        else:  # Forming rectangle
            plain_text += key_matrix[row1][col2]
            plain_text += key_matrix[row2][col1]
    return plain_text

def main():
    key = input("Enter the key for Playfair cipher: ")
    plaintext = input("Enter the plaintext: ")
    encrypted_text = encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)
    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
