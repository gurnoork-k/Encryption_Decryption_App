from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)
def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        return plaintext.decode('ascii')
    except:
        return False
        

nonce, ciphertext, tag = encrypt("hello world")

print("Nonce:     ", nonce)
print("Ciphertext:", ciphertext)
print("Tag:       ", tag)

result = decrypt(nonce, ciphertext, tag)
if result is False:
    print("Decryption failed: data was tampered with")
else:
    print("Decrypted: ", result)
