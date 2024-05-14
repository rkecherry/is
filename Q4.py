import string
import random

def monoalphabetic_encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    for char in text:
        if char.lower() in alphabet:
            idx = alphabet.index(char.lower())
            encrypted_text += key[idx] if char.islower() else key[idx].upper()
        else:
            encrypted_text += char
    return encrypted_text

def monoalphabetic_decrypt(text, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    for char in text:
        if char.lower() in key:
            idx = key.index(char.lower())
            decrypted_text += alphabet[idx] if char.islower() else alphabet[idx].upper()
        else:
            decrypted_text += char
    return decrypted_text

def polyalphabetic_encrypt(text, key):
    alphabet = string.ascii_lowercase
    encrypted_text = ""
    key_len = len(key)
    key_index = 0
    for char in text:
        if char.lower() in alphabet:
            shift = alphabet.index(key[key_index])
            idx = (alphabet.index(char.lower()) + shift) % 26
            encrypted_text += key[(idx + shift) % 26] if char.islower() else key[(idx + shift) % 26].upper()
            key_index = (key_index + 1) % key_len
        else:
            encrypted_text += char
    return encrypted_text

def polyalphabetic_decrypt(text, key):
    alphabet = string.ascii_lowercase
    decrypted_text = ""
    key_len = len(key)
    key_index = 0
    for char in text:
        if char.lower() in alphabet:
            shift = alphabet.index(key[key_index])
            idx = (alphabet.index(char.lower()) - shift) % 26
            decrypted_text += alphabet[idx] if char.islower() else alphabet[idx].upper()
            key_index = (key_index + 1) % key_len
        else:
            decrypted_text += char
    return decrypted_text

def generate_random_key():
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    return ''.join(alphabet)

def main():
    text = input("Enter the text to encrypt: ")
    
    # Generate random keys for both ciphers
    mono_key = generate_random_key()
    poly_key = generate_random_key()

    print("\nMonoalphabetic Encryption:")
    encrypted_text_mono = monoalphabetic_encrypt(text, mono_key)
    print("Encrypted Text:", encrypted_text_mono)
    decrypted_text_mono = monoalphabetic_decrypt(encrypted_text_mono, mono_key)
    print("Decrypted Text:", decrypted_text_mono)

    print("\nPolyalphabetic Encryption:")
    encrypted_text_poly = polyalphabetic_encrypt(text, poly_key)
    print("Encrypted Text:", encrypted_text_poly)
    decrypted_text_poly = polyalphabetic_decrypt(encrypted_text_poly, poly_key)
    print("Decrypted Text:", decrypted_text_poly)

if __name__ == "__main__":
    main()
