from Enigma import ALPHABET, Plugboard, Rotor, Refrector

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

    r = Refrector("BADC")
    i = r.reflect(ALPHABET.index('C'))
    print(ALPHABET[i])