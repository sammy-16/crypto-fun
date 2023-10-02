import hashlib
import os
import base64

def hash_data(data):
    """Hash data using SHA256 and return the first 2 bytes."""
    sha256_hash = hashlib.sha256(data).digest()
    return sha256_hash[:2]

# Assuming the target hash's first 2 bytes are given as a base64 encoded string:
base64_encoded_hash = "a2s="  
decoded_hash = base64.b64decode(base64_encoded_hash)[:2]  # Take first 2 bytes after decoding

target_hash = decoded_hash

collision_data = None
iterations = 0

# Loop until we find a collision
while True:
    # Generate random data (for this example, 16 bytes)
    random_data = os.urandom(16)
    
    # Hash the random data and compare the first 2 bytes to the target
    if hash_data(random_data) == target_hash:
        collision_data = random_data
        break

    iterations += 1
    if iterations % 1000 == 0:
        print(f"Attempted {iterations} hashes...")

if collision_data:
    collision_data_b64 = base64.b64encode(collision_data)
    print(f"Found a collision after {iterations} attempts: {collision_data_b64}")
