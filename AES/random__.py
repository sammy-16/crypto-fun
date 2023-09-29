from Crypto.Util.Padding import pad, unpad

# Padding
data = b"rohansamuelganga"
padded_data = pad(data, 16)

# Unpadding
original_data = unpad(padded_data, 16)

print (data, padded_data, original_data)