#!/usr/bin/python3
from math import gcd
import random

# take two prime numbers as input
print("enter p: ",end="")
p=int(input())
print("enter q: ",end="")
q=int(input())

# calculate n
n=p*q

# print p,q,n
print("p: {}".format(p))
print("q: {}".format(q))
print("n: {}".format(n))

# calculate phi
phi=0
for i in range(1,n+1):
  if gcd(i,n) == 1:
     phi += 1


# print phi
print("phi: {}".format(phi))


# calculate encryption keys
possible_keys=[]
for i in range(2,phi):
    if gcd(i, phi) == 1 and gcd(i, n) == 1:
        possible_keys.append(i)

# print e
e=random.choice(possible_keys)
print("e: {}".format(e))
#print("Possible encryption keys: {}".format(possible_keys))

# calculate private keys
possible_keys=[]
for i in range(phi+1, phi+1000):
    if i*e % phi == 1:
       possible_keys.append(i)
# print d
d=random.choice(possible_keys)
print("d: {}".format(d))
#print("Possible private keys: {}".format(possible_keys))

# enter a random message
print("message: ",end="")
msg=input()

cipher=[]
for char in msg:
    cipher.append(hex(ord(char)**e % n))

# print encrypted message
print("The encrypted message is ")
print(*cipher)

# Decrypt the message
print("The original message is ")
for _ in cipher:
    print(chr(int(_,16)**d % n),end="")
