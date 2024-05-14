import numpy as np
import string

def preprocess_text(text, block_size):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Pad the text if necessary to make its length a multiple of block_size
    while len(text) % block_size != 0:
        text += 'X'
    return text

def text_to_numbers(text):
    alphabet = string.ascii_uppercase
    return [alphabet.index(char) for char in text]

def numbers_to_text(numbers):
    alphabet = string.ascii_uppercase
    return ''.join(alphabet[num] for num in numbers)

def matrix_mod_inverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjugate = (det * np.linalg.inv(matrix)).astype(int)
    return (adjugate * det_inv) % modulus

def hill_cipher_encrypt(plaintext, key):
    block_size = len(key)
    plaintext = preprocess_text(plaintext, block_size)
    key_matrix = np.array(key)
    plaintext_blocks = [text_to_numbers(plaintext[i:i+block_size]) for i in range(0, len(plaintext), block_size)]
    ciphertext_blocks = []
    for block in plaintext_blocks:
        block_vector = np.array(block).reshape(block_size, 1)
        ciphertext_block = np.dot(key_matrix, block_vector) % 26
        ciphertext_blocks.append(ciphertext_block.flatten())
    return ''.join(numbers_to_text(block) for block in ciphertext_blocks)

def hill_cipher_decrypt(ciphertext, key):
    block_size = len(key)
    key_matrix = np.array(key)
    key_inverse = matrix_mod_inverse(key_matrix, 26)
    ciphertext = preprocess_text(ciphertext, block_size)
    ciphertext_blocks = [text_to_numbers(ciphertext[i:i+block_size]) for i in range(0, len(ciphertext), block_size)]
    plaintext_blocks = []
    for block in ciphertext_blocks:
        block_vector = np.array(block).reshape(block_size, 1)
        plaintext_block = np.dot(key_inverse, block_vector) % 26
        plaintext_blocks.append(plaintext_block.flatten())
    return ''.join(numbers_to_text(block) for block in plaintext_blocks)

def main():
    plaintext = input("Enter the plaintext: ")
    key_str = input("Enter the key matrix (e.g., '3 2 1 4' for a 2x2 matrix): ").split()
    key = [int(num) for num in key_str]
    block_size = int(len(key) ** 0.5)
    key = [key[i:i+block_size] for i in range(0, len(key), block_size)]
    
    encrypted_text = hill_cipher_encrypt(plaintext, key)
    decrypted_text = hill_cipher_decrypt(encrypted_text, key)
    
    print("\nHill Cipher Encryption:")
    print("Plaintext:", plaintext)
    print("Encrypted Text:", encrypted_text)

    print("\nHill Cipher Decryption:")
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()
