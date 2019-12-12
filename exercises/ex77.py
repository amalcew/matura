vigenere_letters = {}
vigenere_codes = {}

k = 0
for x in range(65, 91):
    char = chr(x)
    vigenere_letters[char] = k
    k += 1

k = 0
for x in range(65, 91):
    char = chr(x)
    vigenere_codes[k] = char
    k += 1


def encode(message, key):
    message = message.upper()
    key = key.upper()
    message = list(message)
    key = list(key)

    tmp1 = []
    for x in range(len(key)):
        tmp1.append(vigenere_letters[key[x]])

    tmp2 = []
    for x in range(len(message)):
        if message[x] != " " and message[x] != "," and message[x] != ".":
            tmp2.append(vigenere_letters[message[x]])
        else:
            tmp2.append(message[x])
    message = tmp2

    key = []
    n = 0
    line_len = 0
    for x in range(len(message)):
        if message[x] != " " and message[x] != "," and message[x] != ".":
            key.append(tmp1[n % len(tmp1)])
            line_len += 1
        else:
            key.append("")
            n -= 1
        n += 1

    text = []
    for x in range(len(message)):
        code = message[x] + key[x]
        if type(code) is int:
            if code > 25:
                code = code % 25 - 1
                if code < 0:
                    code = 24
            text.append(vigenere_codes[code])
        else:
            text.append(code)
    cipher = ''.join(text)
    iterations = round(line_len / len(tmp1))
    print(cipher)
    return iterations


def decode(message, key):
    message = message.upper()
    key = key.upper()
    message = list(message)
    key = list(key)

    tmp1 = []
    for x in range(len(key)):
        tmp1.append(vigenere_letters[key[x]])

    tmp2 = []
    for x in range(len(message)):
        if message[x] != " " and message[x] != "," and message[x] != ".":
            tmp2.append(vigenere_letters[message[x]])
        else:
            tmp2.append(message[x])
    message = tmp2

    key = []
    n = 0
    line_len = 0
    for x in range(len(message)):
        if message[x] != " " and message[x] != "," and message[x] != ".":
            key.append(tmp1[n % len(tmp1)])
            line_len += 1
        else:
            key.append("")
            n -= 1
        n += 1

    key = []
    n = 0
    for x in range(len(message)):
        if message[x] != " " and message[x] != "," and message[x] != ".":
            key.append(tmp1[n % len(tmp1)])
        else:
            key.append("")
            n -= 1
        n += 1

    text = []
    for x in range(len(message)):
        if type(key[x]) is int:
            code = message[x] - key[x]
            if code < 0:
                code = 26 + code
                if code < 0:
                    code = 24
            text.append(vigenere_codes[code])
        else:
            code = message[x]
            text.append(code)
    cipher = ''.join(text)
    print(cipher)


def ex77_1():
    line = open("data/77/dokad.txt")
    line = line.readline()
    key = "LUBIMYCZYTAC"
    print(encode(line, key))


def ex77_2():
    file = open("data/77/szyfr.txt")
    line = file.readline()
    key = file.readline()
    line = line[:-1]
    key = key[:-1]
    decode(line, key)


def ex77_3():
    file = open("data/77/szyfr.txt")
    line = file.readline()
    word = line.replace(" ", "")
    word = list(word)
    key = file.readline()
    key = list(key)
    key.pop()
    letters = {}
    n = 0
    for x in range(65, 91):
        i = word.count(chr(x))
        letters[chr(x)] = i
        n += i
    k = 0
    for x in range(65, 91):
        l = letters[chr(x)]
        k += l * (l - 1)

    d = round(0.0285/(k/(n*(n-1)) - 0.0385), 2)
    print(d)
    print(len(key))


def test():
    word = "NASX KK"
    key = "EWA"
    decode(word, key)


# test()
ex77_3()
