from Crypto.Cipher import AES
import hashlib

def decrypt_message(iv, ciphertext, key):
    sha256 = hashlib.sha256()
    sha256.update(key)
    derived_key = sha256.digest()
    cipher = AES.new(derived_key, AES.MODE_CBC, iv)

    decrypted_message = cipher.decrypt(ciphertext)

    padding_length = decrypted_message[-1]
    decrypted_message = decrypted_message[:-padding_length]
    return decrypted_message.decode()

def main():
    iv = b'\xa1\xe2\xc3\xaf\xa5\xf6\x8b\xcb\r\xc6e+\x11U;\xb6'
    ciphertext = b'\x9e\xf4\x92\x0f.\x12\xf7\xd7\x0f\xf5\xc9\xcc\xd8\xc5\x83\xe5\xf5\xfa\xd5\xbcZ\x0b\x1dH\x07z\x9c\xa9y\xdf\xfc'
    # Enter the secret key
    key = "secret key"
    decrypted_message = decrypt_message(iv, ciphertext, key.encode())

    print("Decrypted message: " + decrypted_message)

if __name__ == "__main__":
    main()
