def encrypt_rail_fence(plain_text, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    cipher_text = ''.join([''.join(rail) for rail in fence])
    return cipher_text


def decrypt_rail_fence(cipher_text, rails):
    fence = [['\n' for _ in range(len(cipher_text))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if fence[i][j] == '*' and index < len(cipher_text):
                fence[i][j] = cipher_text[index]
                index += 1

    rail = 0
    direction = 1
    plain_text = ''
    for _ in range(len(cipher_text)):
        plain_text += fence[rail][_]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1

    return plain_text


def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    if choice == 'encrypt':
        text = input("Enter the plain text: ")
        rails = int(input("Enter the number of rails: "))
        print("Encrypted text:", encrypt_rail_fence(text, rails))
    else:
        text = input("Enter the cipher text: ")
        rails = int(input("Enter the number of rails: "))
        print("Decrypted text:", decrypt_rail_fence(text, rails))


if __name__ == "__main__":
    main()
