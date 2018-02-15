from Crypto.Hash import SHA256
h = SHA256.new()
h.update(b'hello')
print (h.hexdigest())
