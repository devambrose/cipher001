from crypto.Cipher import AES
from crypto import Random

key = Random.new().read(AES.block_size)
iv = Random.new().read(AES.block_size)

input_file = open("input.jpg")
input_data = input_file.read()
input_file.close()

cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
enc_data = cfb_cipher.encrypt(input_data)

print(enc_data)