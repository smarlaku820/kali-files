#!/usr/bin/python3


#PT -> Orestis - Hacking for fun and profit
#ET -> Pieagnm - Jkoijeg nbw zwx mle grwsnn

PT='OrestisHackingforfunandprofit'
ET='PieagnmJkoijegnbwzwxmlegrwsnn'

import string
alph_u=string.ascii_uppercase


plain_text=list(PT.upper())
cipher_text=list(ET.upper())

cipher_num=[]
plain_num=[]

for _ in plain_text:
    plain_num.append(alph_u.index(_))

for _ in cipher_text:
    cipher_num.append(alph_u.index(_))


diff_num=[]
for i in range(len(cipher_num)):
    diff_num.append((cipher_num[i]-plain_num[i])%26)

print(cipher_num)
print(plain_num)
print(diff_num)


for _ in diff_num:
    print(alph_u[_],end=" ")


