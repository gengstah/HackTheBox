import base64
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

key  = struct.pack('<L', 0x3432e8a3)
key += struct.pack('<L', 0x6191795c)
key += struct.pack('<L', 0x3dd4209e)
key += struct.pack('<L', 0xd5f5f4be)

iv  = struct.pack('<L', 0xe3591f76)
iv += struct.pack('<L', 0x9a95d2d9)
iv += struct.pack('<L', 0xdc5598a7)
iv += struct.pack('<L', 0x6a812006)

enc  = struct.pack('<L', 0xf0251bfe)
enc += struct.pack('<L', 0xca976a80)
enc += struct.pack('<L', 0x58fd8078)
enc += struct.pack('<L', 0x23205cfc)
enc += struct.pack('<L', 0xd0dba26c)
enc += struct.pack('<L', 0xfab502e5)
enc += struct.pack('<L', 0x3aafc0eb)
enc += struct.pack('<L', 0x2c15279f)

backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
decryptor = cipher.decryptor()
print(decryptor.update(enc) + decryptor.finalize())
