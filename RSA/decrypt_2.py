from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
import base64

# Given values
p = 0xb3f9045c4872dd063624064f163e375ec83697828c9678192215b8cda4623c2161388bb446c4460482f0e5024ef8da952252b0e1f9dffb6d2b2798d0d2328306aa8799e4519aaa20216b3bc3acba6c6444764d3e72e4c8f313d4fecadec043b46040929f04655f801c9fd762454d17044c47f26e242cbb4f22530b3499bc386f  # Replace with the given value
q = 0xb3f9045c4872dd063624064f163e375ec83697828c9678192215b8cda4623c2161388bb446c4460482f0e5024ef8da952252b0e1f9dffb6d2b2798d0d2328306aa8799e4519aaa20216b3bc3acba6c6444764d3e72e4c8f313d4fecadec043b46040929f04655f801c9fd762454d17044c47f26e242cbb4f22530b3499c8ab91  # Replace with the given value
e = 0x10001

# Calculate n and phi(n)
n = p * q
phi_n = (p-1) * (q-1)

# Calculate d
d = inverse(e, phi_n)

ciphertext_bytes = base64.b64decode("jIovFgI5yWFV6voFl1nA7Ri2sSR1sIZ7EwtOXdSna+DzFlY8A2pZBUHsgZKWH542Bfja8x0F8RctM+ZOv3zhfhTeaQII9bTQm6CdnT3vpPjMA3dt4jkt+IYLbloyTx2V4saG4yHsJHdbdvudk1AcFrq1Ofn0Nc4q4hUxovalEoN9nYdZaCAyPRX2ptYvOTw+NvBvorTLCIbVKzVw59g/dVI2GyQwDBwVxqOO6bSTcJo1kQWs/S763kfC0dUfneRkYop9y224j8IBhosim4eueo7bKTiGhBQEq3Ba/cPxbH8ttnqizb4rYItfiXAokB4+7jqDVnrSd3rFpMgEF/kJOw==")  # Replace with the given ciphertext

# Decrypt the ciphertext using RSA formula
plaintext_number = pow(int.from_bytes(ciphertext_bytes, "little"), d, n)
plaintext = plaintext_number.to_bytes(256, "little").rstrip(b'\x00')  # Remove potential trailing zero bytes

# Print the result
print(plaintext.decode('ISO-8859-1'))
