# ---------------- RSA IMPLEMENTATION ----------------

# Step 1: Choose two small prime numbers
p = 3
q = 11

# Step 2: Calculate n
n = p * q   # n = 33

# Step 3: Calculate φ(n)
phi = (p - 1) * (q - 1)   # phi = 20

# Step 4: Choose e (must be coprime with phi)
e = 3   # gcd(3,20)=1 so valid

# Step 5: Find d (modular inverse of e)
# (e * d) % phi = 1
d = 7   # because (3*7) % 20 = 1

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))


# ---------------- ENCRYPTION ----------------
def encrypt(message):
    encrypted = []

    for ch in message:
        num = ord(ch)                  # convert character → number
        cipher = (num ** e) % n        # encryption formula
        encrypted.append(cipher)

    return encrypted

# ---------------- DECRYPTION ----------------
def decrypt(cipher_list):
    decrypted = ""

    for num in cipher_list:
        plain = (num ** d) % n         # decryption formula
        decrypted += chr(plain)        # convert number → character

    return decrypted

# ---------------- TEST ----------------
message = "HI"   # you can use your name also

print("\nOriginal Message:", message)


enc = encrypt(message)
print("Encrypted:", enc)

dec = decrypt(enc)
print("Decrypted:", dec)
