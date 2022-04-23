import random
from Enigma import ALPHABET, Plugboard, Rotor, Reflector, EnigmaMachine

if __name__ == "__main__":
    # plugboard = Plugboard("BADC")
    #
    # encrypted_index = plugboard.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[plugboard.backward(encrypted_index)]
    # print(decrypted)

    # rotor = Rotor("BADC", 1)
    #
    # encrypted_index = rotor.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)
    #
    # rotor.rotate()
    #
    # encrypted_index = rotor.forward(ALPHABET.index('A'))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)

    # r = Refrector("BADC")
    # i = r.reflect(ALPHABET.index('C'))
    # print(ALPHABET[i])

    get_random_alphabet = lambda : ''.join(
        random.sample(ALPHABET, len(ALPHABET)))
    print(get_random_alphabet())
    p = Plugboard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 1)

    r = list(ALPHABET)
    index = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(ALPHABET)/2)):
        x = index.pop(random.randint(0, len(index)-1))
        y = index.pop(random.randint(0, len(index)-1))
        r[x], r[y] = r[y], r[x]
    reflector = Reflector(''.join(r))

    machine = EnigmaMachine(
        p, [r1,r2,r3], reflector
    )

    s = "ATTACK SILICON VALLEY"
    e = machine.encrypt(s)
    print(e)
    d = machine.decrypt(e)
    print(d)