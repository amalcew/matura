file1 = open("data/78/wiadomosci.txt")
file1 = file1.readlines()
lines = []
for x in range(len(file1)):
    lines.append(file1[x][:-1])
file2 = open("data/78/podpisy.txt")
file2 = file2.readlines()
fingerprints = []
for x in range(len(file2)):
    fingerprints.append(file2[x][:-1])
public_key = (3, 200)


def hash(message):
    # a
    key = "ALGORYTM"
    s = []
    for x in range(len(key)):
        s.append(ord(key[x]))

    # b
    while True:
        if len(message) % 8 != 0:
            message = message + "."
        else:
            break
    length = len(message)

    # c
    message = list(message)
    index = 0
    for x in range(0, len(message)):
        k = s[index]
        k = (k + ord(message[x])) % 128
        s[index] = k
        index += 1
        if (x+1) % 8 == 0:
            index = 0
    hash_table = s

    # d
    hash = []
    for j in range(0, 8):
        letter = chr(65 + s[j] % 26)
        hash.append(letter)

    hash = ''.join(hash)
    return hash, length, hash_table


def decrypt(encrypted_hash):
    d = public_key[0]
    n = public_key[1]
    if type(encrypted_hash) is str:
        encrypted_hash = encrypted_hash.split()
    encrypted_hash = list(map(int, encrypted_hash))
    tmp = []
    for i in range(0, 8):
        y = encrypted_hash[i]
        x = chr(y * d % n)
        tmp.append(x)
    decrypted_hash = ''.join(tmp)
    return decrypted_hash


def ex78_1():
    print("78.1")
    answer = hash(lines[0])
    print("a) "+str(answer[1]))
    print("b) "+str(answer[2]))
    print("c) "+str(answer[0]))
    print()


def ex78_2():
    print("78.2")
    for x in range(len(lines)):
        answer = hash(lines[x])
        print(str(x+1)+". "+str(answer[0]))
    print()


def ex78_3():
    print("78.3")
    for x in range(len(lines)):
        hsh = hash(lines[x])
        hsh = hsh[0]
        valid_hash = decrypt(fingerprints[x])
        if hsh == valid_hash:
            print(x+1)


ex78_1()
ex78_2()
ex78_3()
