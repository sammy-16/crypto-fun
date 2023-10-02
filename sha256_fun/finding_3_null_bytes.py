import hashlib
import os
import base64

def compute_proof_of_work(challenge_data):
    """
    Compute the proof-of-work for the given challenge_data.
    Return the response_data such that the hash of the 
    concatenated challenge_data and response_data starts with 3 null bytes.
    """
    target_prefix = b'\x00\x00\x00'
    
    counter = 0
    
    while True:
        response_data = counter.to_bytes(4, "big")
        data_to_hash = challenge_data + response_data
        sha256_hash = hashlib.sha256(data_to_hash).digest()
        
        if sha256_hash[:3] == target_prefix:
            return response_data
        
        counter += 1
        if counter % 100000 == 0:
            print(f"Attempted {counter} combinations...")

# Provided challenge in base64
base64_encoded_challenge = "ymd5P7PG8k/4WeH1QMgAeLpkP25xdjnM1CzRAzSAvkM="
challenge_data = base64.b64decode(base64_encoded_challenge)

response = compute_proof_of_work(challenge_data)
response_data = base64.b64encode(response)
print(f"Found response: {response_data.decode('utf-8')}")
