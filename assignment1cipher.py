def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
print("Encrypted:", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted:", decrypted)






