import binascii

# Your byte sequence
key = b'Secr3tKeyForAES!'
iv = bytes([125, 207, 64, 72, 107, 49, 82, 196, 226, 165, 22, 134, 228, 183, 201, 120])

# Convert to hex
key_hex = binascii.hexlify(key).decode('utf-8')
iv_hex = binascii.hexlify(iv).decode('utf-8')

print("Key (hex):", key_hex)
print("IV (hex):", iv_hex)
