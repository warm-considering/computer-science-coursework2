from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

encoded_key = open("privatekey.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase="mully34 is a lad")

data = open("encrypted.txt", "rb")

cipher_rsa = PKCS1_OAEP.new(key)
message = cipher_rsa.decrypt(data.read())
message = message.decode('utf-8')
print(message)
