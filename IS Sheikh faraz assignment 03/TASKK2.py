# Simple ECC (Fixed Version)

p = 17   # prime number (modulus)
a = 2
b = 2

# Point addition
def add(P, Q):
    # If one point is None, return the other
    if P is None:
        return Q
    if Q is None:
        return P

    # If points are same → use doubling
    if P == Q:
        return double(P)

    x1, y1 = P
    x2, y2 = Q

    # If x1 == x2 → vertical line (no inverse possible)
    if (x2 - x1) % p == 0:
        return None   # represents point at infinity

    # slope calculation
    m = ((y2 - y1) * pow(x2 - x1, -1, p)) % p

    # new point
    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p

    return (x3, y3)


# Point doubling
def double(P):
    if P is None:
        return None

    x, y = P

    # If y == 0 → no inverse possible
    if y % p == 0:
        return None

    # slope calculation
    m = ((3*x*x + a) * pow(2*y, -1, p)) % p

    # new point
    x3 = (m*m - 2*x) % p
    y3 = (m*(x - x3) - y) % p

    return (x3, y3)


# Scalar multiplication (k * P)
def multiply(k, P):
    result = None   # start with point at infinity

    for i in range(k):
        result = add(result, P)

    return result


# Base point (valid point on curve)
G = (5, 1)

# Private key (secret)
private_key = 2

# Public key = private_key * G
public_key = multiply(private_key, G)

print("Private Key:", private_key)
print("Public Key:", public_key)


# Simple message
message = 5

# Encryption
k = 2   # random number

C1 = multiply(k, G)                     # first part
C2 = message + multiply(k, public_key)[0]   # second part

print("Encrypted:", (C1, C2))


# Decryption
shared = multiply(private_key, C1)   # shared secret
original = C2 - shared[0]            # recover message

print("Decrypted Message:", original)
