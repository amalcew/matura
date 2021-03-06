# 137
# 465
text = open("data/75/tekst.txt")
text = text.readline()
text = text.split()

letters = {}
k = 0
for x in range(97, 123):
    letters[chr(x)] = k
    k += 1

codes = {}
k = 0
for x in range(97, 123):
    codes[k] = chr(x)
    k += 1


def encode(a, b, letter):
    code = letters[letter]
    code = code * a + b
    if code > 25:
        code = code % 26

    return codes[code]


def extract_key(plain_word, encrypted_word):
    i = len(plain_word)
    keys = []
    for a in range(0, 26):
        for b in range(0, 26):
            code = letters[plain_word[0]] * a + b
            if code > 25:
                code = code % 26

            if code == letters[encrypted_word[0]]:
                key = [a, b]
                keys.append(key)
    print(keys)


def ex75_1():
    for x in range(len(text)):
        word = text[x]
        if word[0] == "d" and word[-1] == "d":
            print(word)


def ex75_2():
    for x in range(len(text)):
        word = text[x]
        if len(word) >= 10:
            tmp = []
            for y in range(len(word)):
                tmp.append(encode(5, 2, word[y]))
            word = "".join(tmp)
            print(word)


def ex75_3():
    sample = open("data/75/probka.txt")
    sample = sample.readlines()
    plain_words = []
    encrypted_words = []
    for x in range(len(sample)):
        tmp = sample[x].split()
        plain_words.append(tmp[0])
        encrypted_words.append(tmp[1])

    index = 0
    extract_key(plain_words[index], encrypted_words[index])
    # extract_key(encrypted_words[index], plain_words[index])

ex75_3()