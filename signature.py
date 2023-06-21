from Crypto.PublicKey import RSA
from Crypto.Hash import SHA512
from Crypto.Signature import pss
r=RSA.generate(2048)
h=SHA512.new(b'Hello',truncate='224')
s=pss.new(r).sign(h)
pss.new(r.publickey()).verify(h,s) # ValueError: Invalid signature