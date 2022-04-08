import string

def caesar_cipher_v1(strings, shift_num):
    result = ''
    for i in strings:
        if i.isupper():
            alphabet = string.ascii_uppercase
        elif i.islower():
            alphabet = string.ascii_lowercase
        else:
            result += i
            continue

        index = (alphabet.index(i) + shift_num) % len(alphabet)
        result += alphabet[index]
    return result

def caesar_cipher_v2(strings, shift_num):
    result = ''
    len_alphabet = ord('Z') - ord('A') + 1
    for i in strings:
        if i.isupper():
            result += chr((ord(i) + shift_num - ord('A')) % len_alphabet + ord('A'))
        elif i.islower():
            result += chr((ord(i) + shift_num - ord('a')) % len_alphabet + ord('a'))
        else:
            result += i

    return result


def decrypt(text):
    len_alphabet = ord('Z') - ord('A') + 1
    for rshift in range(1, len_alphabet+1):
        reverted = ''

        for i in text:
            if i.isupper():
                index = ord(i) - rshift
                if index < ord('A'):
                    index += len_alphabet
                reverted += chr(index)
            elif i.islower():
                index = ord(i) - rshift
                if index < ord('a'):
                    index += len_alphabet
                reverted += chr(index)
            else:
                reverted += i

        yield rshift, reverted




if __name__ == "__main__":
    e = caesar_cipher_v2('Hello my name is Mr.O', 2)
    print(e)
    for rshift, reverted in decrypt(e):
        print(f'Shift {rshift:2d}', reverted)