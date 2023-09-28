import base64

encoded_data = "your_base64_encoded_data"
decoded_data = base64.b64decode(encoded_data)
print(decoded_data.decode('utf-8'))
