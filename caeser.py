def caeser_encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) - 65 + s) % 26 + 65)
        if(char.islower()):
            result += chr((ord(char) -97 + s) % 26 + 97)
        
    return result

def caeser_decrypt(text, shift):
    return caeser_encrypt(text, -shift)

choice = str(input("do you want to encyrpt or decrypt? (E/D)"))
if(choice == "D"):
    text = str(input("enter string you want to encyrpt: "))
    s = int(input("enter shift value: "))
    print("the text: " + text)
    print("the shift: " + str(s))   
    print("cipher text: " + caeser_decrypt(text, s))
else:
    text = str(input("enter string you want to encyrpt: ")) 
    s = int(input("enter shift value: "))
    print("the text: " + text)
    print("the shift: " + str(s))
    print("cipher text: " + caeser_encrypt(text, s))