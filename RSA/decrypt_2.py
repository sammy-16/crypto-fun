from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
import base64

# Given values
p = 0xff5831309060f441563ee3ff68cc5d40871d50f6b3369f13065356a0d7a30304f4a1c65ca017e625769455bb17ad5f2ce3cebc2e36314a038a9bc633838dc3c0118de3551a61662fe9d131942f0f5be93b4c73f2ce91dd3aa7018dec3aa7b693a013a4ac6c0b4b17ce768d617cb96b5c0d142337e1e80f65308602638bb81f69  # Replace with the given value
q = 0xf90fa26c3efa9eee6c05dd2d5f639fba8874f47ed80f5e7877e0b869daa0499d57d0f70c3797c847a9a94b713493bc64267f539f8b2260ea71059769d30a67006085424fc8b287f48e7e7635099606c7da13cb35cb25fe9d17a0cf3503b1758036e314d73059f666bcc5ecc4d49ab89ecbc030c5332f98f93e5be9656b043687  # Replace with the given value
e = 0x10001

# Calculate n and phi(n)
n = p * q
phi_n = (p-1) * (q-1)

# Calculate d
d = inverse(e, phi_n)

ciphertext_bytes = base64.b64decode("daAHVYDZosXm+j4Ty8lpYcupjx7WB3+kzSXn3wqUVZyFIhXW+Qmfig06uI3N6OrzHsAhCi95smEX4L4RS4hx3coMiF/Zldd17Z0lycf0BFafkUYOYxWvR97H8bRmmRKOJieDu6nb8O8GHqG8MDN0mj6UNVG26upPXmeVjmtVPkcWyH7+LRU/XuyyUL1BAu6P1pqjWokslEmp5y3hYnmFav0E2s2Vhkpu8pq0v5/euSk+SJw4UB0eMUVd+SBfbUxUTFhatz6b/Vk7HXLBi8gEuOLPsx9qaMP6ursKCpfD7rD3d7ztzc3uyS2ojAkEUpMfv2O6hqw6Lm/i69KctN46bQ==")  # Replace with the given ciphertext

# Decrypt the ciphertext using RSA formula
plaintext_number = pow(int.from_bytes(ciphertext_bytes, "little"), d, n)
plaintext = plaintext_number.to_bytes(256, "little").rstrip(b'\x00')  # Remove potential trailing zero bytes

# Print the result
print(plaintext.decode('ISO-8859-1'))
