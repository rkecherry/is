import random

def hamming_encode(message):
    # Calculate parity bits
    p1 = message[0] ^ message[1] ^ message[3]
    p2 = message[0] ^ message[2] ^ message[3]
    p3 = message[1] ^ message[2] ^ message[3]

    # Construct the encoded message
    encoded_message = [p1, p2, message[0], p3, message[1], message[2], message[3]]

    return encoded_message

def hamming_decode(encoded_message):
    # Calculate syndrome bits
    s1 = encoded_message[0] ^ encoded_message[2] ^ encoded_message[4] ^ encoded_message[6]
    s2 = encoded_message[1] ^ encoded_message[2] ^ encoded_message[5] ^ encoded_message[6]
    s3 = encoded_message[3] ^ encoded_message[4] ^ encoded_message[5] ^ encoded_message[6]

    # Calculate the error position
    error_position = s3 * 4 + s2 * 2 + s1 - 1

    # Correct the error if possible
    if error_position >= 0:
        encoded_message[error_position] = 1 - encoded_message[error_position]

    # Extract the original message
    decoded_message = [encoded_message[2], encoded_message[4], encoded_message[5], encoded_message[6]]

    return decoded_message

def main():
    # Generate a random 4-bit message
    message = [random.randint(0, 1) for _ in range(4)]
    print("Original Message:", message)

    # Encode the message using Hamming code
    encoded_message = hamming_encode(message)
    print("Encoded Message:", encoded_message)

    # Introduce an error at a random position
    error_position = random.randint(0, 6)
    encoded_message[error_position] = 1 - encoded_message[error_position]
    print("Message with Error:", encoded_message)

    # Decode the message and correct the error if possible
    decoded_message = hamming_decode(encoded_message)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()
