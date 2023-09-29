from Crypto.Cipher import AES
import base64

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

# Provided data
plaintext_prefix_b64 = "rohansamuelganga/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10/x10"
ciphertext = "Yob4WShAPapKs3owB7ugEDqtuZ5XAOMpdTJoBOVuiPzNUD7utfkN2Cawu+MFn7oCVp+PaVooUmD+1WyzXiCNCS4wxt+/pqcFs5b4zpKVcyc="
secret_ciphertext = "uAqYXeBr0ti1ItkcBQWhO0Ll4nlFHGMA8ynnOWGi17ZfE+r7H3t8hSCCbklM/KYnRQN8nbCcwacA42i4R3zYag=="
# Decode from Base64
plaintext_prefix = base64.b64decode(plaintext_prefix_b64)

# Determine the AES key. For this, we will brute-force each possible key until
# we find the one that, when used to encrypt the plaintext prefix, gives us the
# provided ciphertext.
found_key = None
key = None
for i in range(2**24):  # I reduced the loop range for demonstration, 2**128 is infeasible
    cipher = AES.new(i.to_bytes(16, 'big'), AES.MODE_ECB)
    if cipher.encrypt(plaintext_prefix) == ciphertext:
        found_key = i.to_bytes(16, 'big')
        break

if found_key:
    print("Key found!")
    print(f"Original Key: {key}")
    print(f"Found Key: {found_key}")
else:
    print("Key not found")
