def encrypt_rail_fence(text, rails):
    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail] += char
        rail += direction

        if rail == 0 or rail == rails - 1:
            direction *= -1 

    return ''.join(fence)


def decrypt_rail_fence(cipher, rails):
    pattern = [['' for _ in range(len(cipher))] for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher)):
        pattern[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(len(cipher)):
            if pattern[r][c] == '*' and index < len(cipher):
                pattern[r][c] = cipher[index]
                index += 1

    result = ''
    rail = 0
    direction = 1
    for i in range(len(cipher)):
        result += pattern[rail][i]
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return result

if __name__ == "__main__":
    plain_text = "HELLOWORLD"
    rails = 3

    print("원문:", plain_text)
    encrypted = encrypt_rail_fence(plain_text, rails)
    print("암호화 결과:", encrypted)

    decrypted = decrypt_rail_fence(encrypted, rails)
    print("복호화 결과:", decrypted)
