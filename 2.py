from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(1024)
pubkey = keyPair.publickey()
print(f"Public Key: (n={hex(pubkey.n)}, e={hex(pubkey.e)})")

pubKeyPEM = pubkey.exportKey()
print(pubKeyPEM.decode('ascii'))

privKey = keyPair.exportKey()
print(privKey.decode('ascii'))

msg = b'SDSM College'
encryptor = PKCS1_OAEP.new(pubkey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))
