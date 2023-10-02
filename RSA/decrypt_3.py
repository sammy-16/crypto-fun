import gmpy2
import base64

def integer_nth_root(n, e):
    """Find the nth root of an integer using gmpy2"""
    root = gmpy2.iroot(n, e)
    return int(root[0])  # the iroot function returns a tuple (root, exact) where exact is a boolean. 

ciphertext_b64 = "AHC678sqGKCRcyKf/Z2rW7nG+D1E3f1GrV2atIEniW78VUZE7PGIH9+cXEZClI6h46Ysc8QwnVPs2L4lGV4bL4WMjdlI2/a7F6fmvL5b/LXuok9buTshYaMmNOpncDnXv+exq8sYErMcdmVwGbb8Ipe8Tdvg9lrRH3pozTtu2xm8pwqV5cLREo8i3OAg9Ko6A/nIwePeJnr2w6MxggQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="  # Replace with the given ciphertext
ciphertext = base64.b64decode(ciphertext_b64)
ciphertext_int = int.from_bytes(ciphertext, "little")

plaintext_int = integer_nth_root(ciphertext_int, 3)
plaintext_bytes = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, 'little')

# Now, since you don't know if the plaintext will be valid UTF-8, try decoding.
# If it fails, then maybe the bytes are a clue or need further processing.
try:
    flag = plaintext_bytes.decode('utf-8')
    print(flag)
except UnicodeDecodeError:
    print("Could not decode as UTF-8, printing the bytes:")
    print(plaintext_bytes)
