def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Enter the text to encrypt: ")
    shift = 3
    encrypted_message = caesar_cipher(message, shift)
    print("Encrypted:", encrypted_message)

    decrypted_message = caesar_cipher(encrypted_message, -shift)
    print("Decrypted:", decrypted_message)
