def ex6_1():
    file = open("Data/dane_6_1.txt", "r")
    words = []
    k = 107
    for x in range(0, 100):
        word = file.readline()
        word = word[:-1]
        words.append(word)

    for x in range(len(words)):
        encrypted = []
        tmp = []
        print(words[x])
        # char encryption
        for y in range(len(words[x])):
            ascii_code = ord(words[x][y])
            k_tmp = k
            while k_tmp:
                ascii_code += 1
                if ascii_code > 90:
                    ascii_code = 65
                k_tmp -= 1
            encrypted.append(ascii_code)

        # translating to word
        for z in range(len(encrypted)):
            tmp.append(chr(encrypted[z]))

        print(''.join(tmp))
        print()
    file.close()


def ex6_2():
    file = open("Data/dane_6_2.txt", "r")
    words = []
    keys = []
    for x in range(0, 3000):
        line = file.readline()
        tmp = line.split()
        words.append(tmp[0])
        keys.append(int(tmp[1]))

    for y in range(0, 3000):
        decrypted = []
        tmp = []
        encrypted_word = words[y]
        key = keys[y]
        print(encrypted_word)
        for z in range(len(encrypted_word)):
            ascii_code = ord(encrypted_word[z])
            key_tmp = key
            while key_tmp:
                ascii_code -= 1
                if ascii_code < 65:
                    ascii_code = 90
                key_tmp -= 1
            decrypted.append(ascii_code)
        # translating to word
        for z in range(len(decrypted)):
            tmp.append(chr(decrypted[z]))

        print(''.join(tmp))
        print()
    file.close()


def ex6_3():
    pass

# ex6_1()
# ex6_2()
