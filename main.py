from caeser import caeser_encrypt, caeser_decrypt
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
            print("Encrypted:", caeser_encrypt(text, shift))

        elif choice == '2':
            text = input("Enter text to decrypt: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted:", caeser_decrypt(text, shift))

        elif choice == '3':
            text = input("Enter text to encrypt: ")
            nonce, ciphertext, tag = aes_encrypt(text)
            print("Encrypted:")
            print(f"Nonce: {nonce.hex()}")
            print(f"Ciphertext: {ciphertext.hex()}")
            print(f"Tag: {tag.hex()}")

        elif choice == '4':
            nonce = bytes.fromhex(input("Enter nonce (hex): "))
            ciphertext = bytes.fromhex(input("Enter ciphertext (hex): "))
            tag = bytes.fromhex(input("Enter tag (hex): "))
            decrypted = aes_decrypt(nonce, ciphertext, tag)
            if decrypted:
                print("Decrypted:", decrypted)
            else:
                print("Decryption failed: message is corrupt or wrong key.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
