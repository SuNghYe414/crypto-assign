import string
import random

def generate_key():
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled)), dict(zip(shuffled, letters))

def mono_encrypt(text, key_map):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += key_map[char]
        else:
            result += char
    return result

def mono_decrypt(text, reverse_key_map):
    return mono_encrypt(text, reverse_key_map)

key_map, reverse_key_map = generate_key()

plain_text = "MARIO WORLD"
encrypted = mono_encrypt(plain_text, key_map)
decrypted = mono_decrypt(encrypted, reverse_key_map)

print("Mono 암호화:", encrypted)
print("Mono 복호화:", decrypted)
