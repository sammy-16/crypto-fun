import base64

# Given Base64 encoded OTP and ciphertext
encoded_otp = "+gcdzy8mAxRLUrO9iRqFAQk/m6SNTDNJnTYTzsmzenTLaeK9PO91A1tjIoQITUbSpg0OFg=="  # Replace with your Base64 encoded OTP
encoded_ciphertext = "inBz4UxJb3guNdbG0G3DZWZg6sf/OUEB0GkhovzJLjOqBInaCbUZLQo7EfNbAzyb3FpzHA=="  # Replace with your Base64 encoded ciphertext

# Decoding Base64 to bytes
otp = base64.b64decode(encoded_otp)
ciphertext = base64.b64decode(encoded_ciphertext)

# XORing the OTP with the ciphertext to get the original plaintext
plaintext_bytes = bytes([otp_byte ^ cipher_byte for otp_byte, cipher_byte in zip(otp, ciphertext)])

# Converting bytes to string
plaintext = plaintext_bytes.decode('utf-8')

print("Decrypted plaintext:", plaintext)
