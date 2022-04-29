#!/usr/bin/python3

import hashlib

# password in its own variable 
password="O9mxdf12&s=X_7129nsd"

# generating an md5 hash
md5_hash_obj=hashlib.md5(password.encode())

# printing the hash in bytes & hexdecimal 
print("md5 hash\n")
print(md5_hash_obj.digest())
print(md5_hash_obj.hexdigest())
print()

# generating a sha1 hash
sha1_hash_obj=hashlib.sha1(password.encode())

# printing the hash in bytes & hexadecimal
print("sha1 hash\n")
print(sha1_hash_obj.digest())
print(sha1_hash_obj.hexdigest())
print()

# generating a sha512 hash
sha512_hash_obj=hashlib.sha512(password.encode())

# printing the hash in bytes & hexadecimal
print("sha512 hash\n")
print(sha512_hash_obj.digest())
print(sha512_hash_obj.hexdigest())
print()

