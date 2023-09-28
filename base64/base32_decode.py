import base64

encoded_data = "your_base32_encoded_data===="
decoded_data = base64.b32decode(encoded_data)
print(decoded_data.decode('utf-8'))
