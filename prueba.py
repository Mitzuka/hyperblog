import binascii

ars = 'man'
ref = binascii.hexlify(ars)
print(ref)