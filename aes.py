# Authors: Anna Vyzentini & Stefanos-Marios Daniil


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import random,string

CC=random.randint(0,9999999999999999)
binCC=bin(CC)

while (len(binCC)!=54):
    CC=random.randint(0,9999999999999999)
    binCC=bin(CC)

L=binCC[0:27]
R=binCC[27:]

#i=0
l0=str(L).encode()
r0=str(R).encode()
k0 = get_random_bytes(16)
l1=r0
cipher= AES.new(k0, AES.MODE_CFB)
f= cipher.encrypt(r0)
r1= bytes(x ^ y for x, y in zip(l0, f))

#i=1
k1= get_random_bytes(16)
l2=r1
cipher= AES.new(k1, AES.MODE_CFB)
f= cipher.encrypt(r1)
r2=bytes(x^y for x,y in zip(l1,f))

#i=2
k2=get_random_bytes(16)
l3=r2
cipher= AES.new(k2, AES.MODE_CFB)
f= cipher.encrypt(r2)
r3=bytes(x^y for x,y in zip(l2,f))

#i=3
k3=get_random_bytes(16)
l4=r3
cipher= AES.new(k3, AES.MODE_CFB)
f= cipher.encrypt(r3)
r4=bytes(x ^ y for x,y in zip(l3,f) )

c=l4+r4
