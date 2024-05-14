def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def main():
    text = input("Enter the text to be encrypted/decrypted: ")
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    encrypted_text = caesar_cipher(text, shift)
    print("Result:", encrypted_text)

if __name__ == "__main__":
    main()
