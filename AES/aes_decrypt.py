from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

# Provided data
plaintext_prefix_b64 = "00000000000000000000000000000000{}{}"
for i in range(100):
    for j in range(100):
        plaintext_prefix = plaintext_prefix_b64.format(str(i).zfill(2), str(j).zfill(2)).encode()
        # Determine the AES key. For this, we will brute-force each possible key until
        # we find the one that, when used to encrypt the plaintext prefix, gives us the
        # provided ciphertext.
        found_key = None
        key = None
        for k in range(2**24):  # Reduced the loop range for demonstration, 2**128 is infeasible
            cipher = AES.new(k.to_bytes(16, 'little'), AES.MODE_ECB)
            encrypted_data = cipher.encrypt(pad(plaintext_prefix, AES.block_size))
            if encrypted_data == ciphertext:
                found_key = k.to_bytes(16, 'little')
                break

        if found_key:
            print("Key found!")
            print(f"Found Key: {found_key}")
            break
    else:
        continue
    break
else:
    print("Key not found")
secret_ciphertext = base64.b64decode("8o3H1KIzMwY1n+rdtz8+bG/xo/qRBMFF6HP0J9+U3Q4MQkVmbnzaBuXN+vBY2doEviz0NvpHh8n+hvwNmlST0A==")
ciphertext = base64.b64decode("ZgKK1/oussAypNOvYB60ZnxvDcU5F6PWrX+K6mmUPe74ge3xOojyNZDArmNLq/mYY7pdFFgTy4CPdHH2aQ8GZCvCGhXkTWnai8PjR6S+QUQ=")
plaintext_prefix = base64.b64decode(plaintext_prefix_b64)

# Determine the AES key. For this, we will brute-force each possible key until
# we find the one that, when used to encrypt the plaintext prefix, gives us the
# provided ciphertext.
found_key = None
key = None
for i in range(2**24):  # Reduced the loop range for demonstration, 2**128 is infeasible
    cipher = AES.new(i.to_bytes(16, 'little'), AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(plaintext_prefix, AES.block_size))
    if encrypted_data == ciphertext:
        found_key = i.to_bytes(16, 'little')
        break

if found_key:
    print("Key found!")
    print(f"Found Key: {found_key}")
else:
    print("Key not found")
