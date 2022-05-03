#Encryption

## Key Terms
- Cipher
- Ciphertext
- Plaintext
- Cryptanalysis
- Encoding
- Encryption
- Key
- Passphrase
- Asymmetric Encryption
- Symmetric Encryption
- BruteForce

Symmetric key encryption is faster than Asymmetric key encryption.
AES, DES(broken) are examples of Symmetric key encryption.
Symmetric keys are usually shorter.
AES uses 128,256 bit keys.
DES uses 56 bit keys. DES cannot be trusted anymore.

RSA, eliptic curve cryptography are examples of Asymmetric key encryption.
RSA uses 2048 to 4096 bit keys.
In Asymmetric key encryption, two keys are used. public/private keys.

RSA (Rivest Shamir Adleman)
RSA is based on the mathematically difficult problem of finding factors of a large number.
It is often difficult to find out what two prime numbers should be brought together to be multiplied &
give a resultant or expected number ?

The key variables that you need to know about for RSA in CTFs are p, q, m, n, e, d, and c.
p,q are two large prime numbers
n = p * q (product of p,q)
phi = no of co-primes to n from [1,n]
e = Any integer which is co-prime to both n, phi
d = Any integer which satisfies (integer\*e % phi == 1) & often > phi & possible keys fall in (phi, phi+1000)
public key = (e,n)
private key = (d,n) 
m = message in plaintext
c = cipher text (encrypted plaintext)

RSA CTF challenges
- [RSA CTF Tool](https://github.com/Ganapati/RsaCtfTool)
- [RSA Tool](https://github.com/ius/rsatool)

## References
- [3DES and DES Encryption](https://www.comparitech.com/blog/information-security/3des-encryption/#The_history_of_3DES_encryption)
- [Math Behind RSA Encryption](https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/)
- [How HTTP(s) work](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)

