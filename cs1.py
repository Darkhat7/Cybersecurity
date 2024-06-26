def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decryption is just encryption with negative shift

def main():
    while True:
        print("\n=== Caesar Cipher ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (a positive integer): "))
            encrypted_text = caesar_cipher_encrypt(plaintext, shift)
            print(f"Encrypted message: {encrypted_text}")

        elif choice == '2':
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (a positive integer): "))
            decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
            print(f"Decrypted message: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
