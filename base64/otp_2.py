import base64

def xor_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

# Base64 encoded ciphertext and OTP
ciphertext_b64 = "BASE64_ENCODED_CIPHERTEXT_HERE"
otp_b64 = "BASE64_ENCODED_OTP_HERE"

# Decode from base64
ciphertext = base64.b64decode(ciphertext_b64)
otp = base64.b64decode(otp_b64)

# Ensure lengths match
if len(ciphertext) != len(otp):
    raise ValueError("Ciphertext and OTP lengths do not match!")

# Decrypt by XORing
plaintext = xor_bytes(ciphertext, otp)

print(plaintext.decode('utf-8'))  # Assuming the original plaintext was UTF-8 encoded
