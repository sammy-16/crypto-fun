import base64
from pwn import *

def recv_ciphertext(proc) -> bytes:
    proc.recvuntil(b"ciphertext (b64): ")
    ciphertext = proc.recvuntil(b"\n").strip(b"\n")
    ciphertext = base64.b64decode(ciphertext)
    return ciphertext

def send_plaintext(proc, prefix: bytes) -> None:
    proc.recvuntil(b"plaintext prefix (b64): ")
    proc.sendline(base64.b64encode(prefix))

def main():
    proc = process("/challenge/run.py")
    previous_byte_flags = b""
    for i in range(96):
        for byt in range(0, 256):
            byt = bytes([byt])
            # prefix = b"\x00" * 15 + byt + b"\x00" * 15
            prefix_chunk0 =  b"\x00" * (95 - len(previous_byte_flags)) + previous_byte_flags + byt
            prefix_chunk1 =  b"\x00" * (95 - len(previous_byte_flags))


            send_plaintext(proc, prefix_chunk0  + prefix_chunk1)
            cipher = recv_ciphertext(proc)
            chunk0 = cipher[:96]
            chunk1 = cipher[96:192]
            if chunk0 == chunk1:
                previous_byte_flags += byt
                print(previous_byte_flags )
                break
            else:
                pass

if __name__ == "__main__":
    main()