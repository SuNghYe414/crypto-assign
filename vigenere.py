def vigenere_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            result += chr((ord(char) - 65 - shift + 26) % 26 + 65)
            key_index += 1
        else:
            result += char
    return result

plain_text = "MARIO WORLD"
key = "KEY"

encrypted = vigenere_encrypt(plain_text, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Vigenère 암호화:", encrypted)
print("Vigenère 복호화:", decrypted)
