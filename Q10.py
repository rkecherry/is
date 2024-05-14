import random

# Function to encrypt the plaintext using a simple substitution cipher
def encrypt(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            encrypted_text += key[char]
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the ciphertext using a simple substitution cipher
def decrypt(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            for k, v in key.items():
                if v == char:
                    decrypted_text += k
        else:
            decrypted_text += char
    return decrypted_text

# Function to generate a random substitution key
def generate_key():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    key = {alphabet[i]: shuffled_alphabet[i] for i in range(len(alphabet))}
    return key

# Ciphertext-only attack
def ciphertext_only_attack(ciphertext):
    decrypted_text = ""
    # Known substitution key
    known_key = {'E': 'T', 'T': 'H', 'H': 'E'}
    for char in ciphertext:
        if char.isalpha():
            if char in known_key.values():
                for k, v in known_key.items():
                    if v == char:
                        decrypted_text += k
            else:
                decrypted_text += "?"
        else:
            decrypted_text += char
    return decrypted_text

# Known-plaintext attack
def known_plaintext_attack(ciphertext, known_plaintext, known_ciphertext):
    decrypted_text = ""
    # Generate the key using the known plaintext and ciphertext
    key = {}
    for i in range(len(known_plaintext)):
        key[known_plaintext[i]] = known_ciphertext[i]
    
    for char in ciphertext:
        if char.isalpha():
            if char in key.values():
                for k, v in key.items():
                    if v == char:
                        decrypted_text += k
            else:
                decrypted_text += "?"
        else:
            decrypted_text += char
    return decrypted_text

# Take input from the user
plaintext = input("Enter the plaintext: ").upper()
ciphertext = encrypt(plaintext, generate_key())
print("Ciphertext:", ciphertext)

# Ciphertext-only attack
print("\nCiphertext-only attack:")
recovered_text = ciphertext_only_attack(ciphertext)
print("Recovered text:", recovered_text)

# Known-plaintext attack
print("\nKnown-plaintext attack:")
known_plaintext = input("Enter a known part of the plaintext: ").upper()
known_ciphertext = input("Enter the corresponding part of the ciphertext: ").upper()
recovered_text = known_plaintext_attack(ciphertext, known_plaintext, known_ciphertext)
print("Recovered text:", recovered_text)
