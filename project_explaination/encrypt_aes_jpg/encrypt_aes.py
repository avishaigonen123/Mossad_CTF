from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Encryption key and initialization vector as arrays of integers
KEY = b'Secr3tKeyForAES!'
IV =   [125, 207, 64, 72, 107, 49, 82, 196, 226, 165, 22, 134, 228, 183, 201, 120]
# Convert arrays to bytes
key = bytes(KEY)
iv = bytes(IV)

input_file_path = r"final.jpg"
output_file_path = r"final_encrypted.jpg"

with open(input_file_path, 'rb') as input_file:
    plaintext = input_file.read()

# Create an AES cipher object
cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

# Encrypt the padded plaintext
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext)

# Write the ciphertext to the output file in binary mode
with open(output_file_path, 'wb') as output_file:
    output_file.write(ciphertext)

print("Encryption completed. Ciphertext written to:", output_file_path)
