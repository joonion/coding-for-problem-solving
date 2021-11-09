from Crypto.Util.number import getPrime, inverse
from secret import flag

bits = 512
p = getPrime(bits * 1)
q = getPrime(bits * 2)
r = getPrime(bits * 4)
n = p * q * r
e = 0x10001

pt = int.from_bytes(flag, 'big')
ct = pow(pt, e, n)

pq = inverse(p * q, r)
qr = inverse(q * r, p)
rp = inverse(r * p, q)

print(f"n = {n}")
print(f"e = {e}")
print(f"pq = {pq}")
print(f"qr = {qr}")
print(f"rp = {rp}")
print(f"ct = {ct}")
