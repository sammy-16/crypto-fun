from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64encode, b64decode

# Mock functions (replace with actual functions from your challenge context if needed)
def get_random_bytes(size):
    import os
    return os.urandom(size)

def show_b64(description, content):
    print(f"{description}: {b64encode(content).decode('utf-8')}")

# Input your known secret ciphertext here
known_secret_ciphertext_b64 = input("Enter your known secret ciphertext (in base64): ")
known_secret_ciphertext = b64decode(known_secret_ciphertext_b64)

# Attack starts here
known_flag = b""
block_size = 16

while True:  # until we've decrypted the full flag
    prefix_length = block_size - 1 - len(known_flag) % block_size
    
    # Input your plaintext prefix
    plaintext_prefix_b64 = input(f"Enter plaintext prefix (of length {prefix_length} bytes, in base64): ")
    plaintext_prefix = b64decode(plaintext_prefix_b64)
    
    # Input the resulting ciphertext after the plaintext prefix is combined with the flag
    resulting_ciphertext_b64 = input("Enter resulting ciphertext (in base64) for the provided prefix: ")
    resulting_ciphertext = b64decode(resulting_ciphertext_b64)
    
    block_to_compare = (len(plaintext_prefix) + len(known_flag)) // block_size

    found = False
    for possible_byte in range(256):  # Try every possible byte value
        brute_plaintext = plaintext_prefix + known_flag + bytes([possible_byte])
        brute_ciphertext = pad(brute_plaintext, AES.block_size)  # This line should be adjusted according to how encryption is done in the challenge.
        
        # Compare the guessed block of our brute-forced ciphertext with the block in the resulting ciphertext
        if brute_ciphertext[block_size * block_to_compare : block_size * (block_to_compare + 1)] == resulting_ciphertext[block_size * block_to_compare : block_size * (block_to_compare + 1)]:
            known_flag += bytes([possible_byte])
            found = True
            break

    if not found:
        print("Couldn't find the next byte. Ending.")
        break

print(f"Decrypted flag: {known_flag.decode('utf-8')}")
