from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

filepu = open("publickey.bin", "rb")
print (filepu)

file_out = open("encrypted.txt", "wb")
recipient_key = RSA.import_key(filepu.read())

cipher_rsa = PKCS1_OAEP.new(recipient_key)
print(cipher_rsa.encrypt(bytes("dave", 'utf-8')))
file_out.write(cipher_rsa.encrypt(bytes("dave", 'utf-8')))
file_out.close()
