def caeser_encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)
        else:
            result += char  # keep non-alphabetic characters as is
    return result

def caeser_decrypt(text, s):
    return caeser_encrypt(text, -s)
if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (E/D): ").strip().lower()

    if choice == "d":
        text = input("Enter the string you want to decrypt: ")
        s = int(input("Enter shift value: "))
        print("The text:", text)
        print("The shift:", s)
        print("Decrypted text:", caeser_decrypt(text, s))
    elif choice == "e":
        text = input("Enter the string you want to encrypt: ")
        s = int(input("Enter shift value: "))
        print("The text:", text)
        print("The shift:", s)
        print("Encrypted text:", caeser_encrypt(text, s))
    else:
        print("Invalid choice. Please enter E or D.")
