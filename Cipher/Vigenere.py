import string

ALPHABET = string.ascii_uppercase


def generate_key(message, keyword):

    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        keyword += keyword[i]

    return keyword

def encrypt(message, key):
    result = ''
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue
        # index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        # result += ALPHABET[index]
        result += chr((ord(message[i]) + ord(key[i])) % len(ALPHABET) + ord('A'))
    return result

def decrypt(cipher, key):
    result = ''
    for i, char in enumerate(cipher):
        if char not in ALPHABET:
            result += char
            continue
        # index = (ALPHABET.index(char) - ALPHABET.index(key[i]) + len(ALPHABET)) % len(ALPHABET)
        # result += ALPHABET[index]
        result += chr((ord(cipher[i]) - ord(key[i]) + len(ALPHABET)) % len(ALPHABET) + ord('A'))
    return result

if __name__ == "__main__":
    text = 'ATTACK SILICON VALLEY'
    k = generate_key(text, 'HELLO')
    e = encrypt(text, k)
    print(e)
    d = decrypt(e, k)
    print(d)