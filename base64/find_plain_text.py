import base64

def xor(data, key):
    return bytes([d ^ k for d, k in zip(data, key)])

# Decode from Base64
plaintext_b64 = "VIEYBERVCNREOIUCNVERUBV9URGFBUIERGIUYBREUYIVGYERGBCVIUEWRBVCYIECRYCV"
ciphertext_b64 = "dt5Fr/cG5YqnRcQEUch9VpqcDQAQk+kKimnpgP0PHN4N6rmuRHKGj9PWoy7M7EGLduxZ"
secret_b64 = "UigzhdA8gTKGGiR9Ke5ddseKOGG42e5/o13PkKF4N3FzkUjsEilLgMOY00zdwrrASTuxtQ=="

plaintext = base64.b64decode(plaintext_b64)
ciphertext = base64.b64decode(ciphertext_b64)
secret = base64.b64decode(secret_b64)

# Derive the one-time pad from the provided plaintext and its ciphertext
derived_pad = xor(plaintext, ciphertext)

# Decrypt the secret ciphertext using the derived pad
decrypted_message = xor(derived_pad, secret)

print(decrypted_message.decode('utf-8'))
