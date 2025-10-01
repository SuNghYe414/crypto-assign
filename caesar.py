def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

plain_text = "MARIO WORLD"
shift = 3

encrypted = caesar_encrypt(plain_text, shift)
decrypted = caesar_decrypt(encrypted, shift)

print("Caesar 암호화:", encrypted)
print("Caesar 복호화:", decrypted)
