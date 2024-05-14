def encrypt(text, key):
    encrypted_text = [''] * len(key)
    
    # Arrange the text based on the key
    for i in range(len(key)):
        encrypted_text[key[i] - 1] = text[i]
    
    return ''.join(encrypted_text)

def decrypt(text, key):
    decrypted_text = [''] * len(key)
    
    # Rearrange the text based on the key
    for i in range(len(key)):
        decrypted_text[i] = text[key[i] - 1]
    
    return ''.join(decrypted_text)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        key = list(map(int, input("Enter the encryption key (sequence of numbers from 1 to n separated by spaces): ").split()))
        if sorted(key) != list(range(1, len(key) + 1)):
            print("Invalid key. Key should be a sequence of numbers from 1 to n.")
            return
        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        text = input("Enter the text to decrypt: ")
        key = list(map(int, input("Enter the decryption key (sequence of numbers from 1 to n separated by spaces): ").split()))
        if sorted(key) != list(range(1, len(key) + 1)):
            print("Invalid key. Key should be a sequence of numbers from 1 to n.")
            return
        decrypted_text = decrypt(text, key)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
