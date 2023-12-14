import hashlib
result = hashlib.md5 (b'Priya')
result1 = hashlib.md5 (b'Diya')
print ("The byte equivalent of hash is :", end ="")
print(result.digest ())
print ("The byte equivalent of hash is :", end ="")
print (result1.digest () )

import hashlib
str = input("Enter the value to encode")
result = hashlib.sha1(str.encode())
print("The Hexadecimal Equivalent if SHA1 is: ")
print(result.hexdigest())
