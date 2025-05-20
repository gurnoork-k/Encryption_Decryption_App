from caeser import caesar_encrypt, caesar_decrypt
from exaes import aes_encrypt, aes_decrypt

def main():
    while True:
        print("\n==== Encryption & Decryption App ====")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt")
        print("3. AES Encrypt")
        print("4. AES Decrypt")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted:", caesar_encrypt(text, shift))

        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted:", caesar_decrypt(text, shift))

        elif choice == '3':
            text = input("Enter text to encrypt: ")
            password = input("Enter password: ")
            print("Encrypted (Base64):", aes_encrypt(text, password))

        elif choice == '4':
            enc = input("Enter Base64 encrypted text: ")
            password = input("Enter password: ")
            print("Decrypted:", aes_decrypt(enc, password))

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-5.")

main()
