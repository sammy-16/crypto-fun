import base64

hex_input = input("Enter a hex string: ")
byte_input = bytes.fromhex(hex_input)
base64_output = base64.b64encode(byte_input).decode('utf-8')

print("Base64 output:", base64_output)
