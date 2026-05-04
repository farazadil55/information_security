import hashlib

# ---------------- RSA KEY GENERATION ----------------
p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 3
d = 7

print("Public Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))


# ---------------- CREATE HASH ----------------
def get_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()


# ---------------- SIGN MESSAGE ----------------
def sign(message):
    hash_value = get_hash(message)
    hash_int = int(hash_value, 16)     # convert hex → integer
    signature = pow(hash_int, d, n)    # encrypt hash with private key
    return signature


# ---------------- VERIFY SIGNATURE ----------------
def verify(message, signature):
    new_hash = get_hash(message)
    new_hash_int = int(new_hash, 16)

    decrypted_hash = pow(signature, e, n)  # decrypt using public key

    return new_hash_int % n == decrypted_hash


# ---------------- TEST ----------------
message = "HELLO"

print("\nOriginal Message:", message)

signature = sign(message)
print("Signature:", signature)

result = verify(message, signature)
print("Verification (original):", result)


# ---------------- MODIFIED MESSAGE TEST ----------------
fake_message = "HELLOO"   # changed message

result2 = verify(fake_message, signature)
print("Verification (modified message):", result2)
