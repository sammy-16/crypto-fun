from Crypto.Cipher import AES
import base64

def decrypt_aes_ecb(ciphertext_b64, key_b64):
    # Decode from base64
    ciphertext = base64.b64decode(ciphertext_b64)
    key = base64.b64decode(key_b64)

    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the plaintext
    plaintext_bytes = cipher.decrypt(ciphertext)
    
    # Since you mentioned you want to avoid using unpad, and if you're sure 
    # the plaintext was UTF-8 encoded and doesn't end with any padding bytes:
    try:
        plaintext = plaintext_bytes.decode('utf-8')
        return plaintext
    except UnicodeDecodeError:
        print("Decryption successful, but the result is not valid UTF-8.")
        return None

# Example usage
ciphertext_b64 = "NqaVSEpJsJMtG3yGA7aDpLzgTeWaMi0aWU/QmXypMnHoX46F3hg+BNKSmCl3xSck1pjt25MgldGCJ+hkmlgVyg=="
key_b64 = "yAKf9pdTmNNwmbxTHcALsw=="
plaintext = decrypt_aes_ecb(ciphertext_b64, key_b64)
print(plaintext)
