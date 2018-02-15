from Crypto.PublicKey import RSA


key = RSA.generate(2048)

filepr = open("privatekey.bin", "wb")
filepu = open("publickey.bin", "wb")

binprivkey = key.exportKey(passphrase="mully34 is a lad", pkcs=8, protection="scryptAndAES128-CBC")
print (binprivkey)
filepr.write(binprivkey)

binpubkey =  key.publickey().exportKey()
print (binpubkey)
filepu.write(binpubkey)

filepr.close()
filepu.close()
