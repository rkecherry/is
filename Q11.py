def stream_cipher(text, key, mode):
    key_length = len(key)
    text_length = len(text)
    result = ""
    for i in range(text_length):
        key_index = i % key_length
        if mode == 'encrypt':
            result += chr((ord(text[i]) + ord(key[key_index])) % 256)
        elif mode == 'decrypt':
            result += chr((ord(text[i]) - ord(key[key_index])) % 256)
    return result

# Take input from the user
text = input("Enter the text: ")
key = input("Enter the key: ")

# Encrypt the text
encrypted_text = stream_cipher(text, key, 'encrypt')
print("Encrypted text:", encrypted_text)

# Decrypt the encrypted text
decrypted_text = stream_cipher(encrypted_text, key, 'decrypt')
print("Decrypted text:", decrypted_text)
