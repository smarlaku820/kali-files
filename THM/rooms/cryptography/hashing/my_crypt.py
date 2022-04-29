#!/usr/bin/python3
import crypt

password="ksdfkj12esf"

print("MD5 Hash")
md5_hash=crypt.crypt(password, crypt.METHOD_MD5)
print(md5_hash+"\n")

print("SHA512 Hash")
sha512_hash=crypt.crypt(password, crypt.METHOD_SHA512)
print(sha512_hash+"\n")

print("SHA256 Hash")
sha256_hash=crypt.crypt(password, crypt.METHOD_SHA256)
print(sha256_hash+"\n")
reversed_hash=crypt.crypt(password, sha256_hash)
print(reversed_hash+"\n")
