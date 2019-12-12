def encode(message, cipher):
    # message = message.upper()
    n = len(cipher)
    if len(message) >= n:
        # print("0. " + message)
        for i in range(1, len(message)+1):
            q = cipher[(i-1) % n]
            tmp = list(message)
            tmp[i-1], tmp[q-1] = tmp[q-1], tmp[i-1]
            message = ''.join(tmp)
            # print(str(i)+". "+message)
    else:
        message = None
    return message


def ex76_1():
    file = open("data/76/szyfr1.txt")
    file = file.readlines()
    plain_texts = []
    for x in range(len(file)-1):
        line = file[x].split()
        plain_texts.append(line[0])

    cipher = file[-1]
    cipher = cipher.split()
    cipher = list(map(int, cipher))

    for x in range(len(plain_texts)):
        ciphertext = encode(plain_texts[x], cipher)
        print(ciphertext)


def ex76_2():
    file = open("data/76/szyfr2.txt")
    file = file.readlines()
    plain_text = file[0]
    plain_text = plain_text.split()
    plain_text = ''.join(plain_text)

    cipher = file[-1]
    cipher = cipher.split()
    cipher = list(map(int, cipher))

    ciphertext = encode(plain_text, cipher)
    print(ciphertext)


def ex76_3():
    file = open("data/76/szyfr3.txt")
    file = file.readlines()
    plain_text = file[0]
    plain_text = plain_text.split()
    plain_text = ''.join(plain_text)
    cipher = [6, 2, 4, 1, 5, 3]

    ciphertext = encode(plain_text, cipher)
    if ciphertext == "csonozolzhcynadyrutkurtsymtyroglaakytamrofniarutam":
        print(True)
    else:
        print(False)


ex76_3()