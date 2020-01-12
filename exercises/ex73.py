file = open("data/73/tekst.txt")
line = file.readline()
words = line.split()
letters = list(''.join(words))


def zad1():
    test = []
    for x in range(len(words)):
        word = words[x]
        flag = False
        for y in range(len(word) - 1):
            a = word[y]
            b = word[y+1]
            if ord(b) - ord(a) == 0:
                flag = True
        if flag:
            test.append(word)

    print("73.1 - "+str(len(test)))
    print()


def zad2():
    print("74.2: ")
    l = len(letters)
    for x in range(65, 91):
        letter = chr(x)
        how_many = letters.count(letter)
        percent = " ("+str(round((how_many/l)*100, 2))+"%)"
        print(letter+": "+str(how_many)+percent)
    print()


def zad3():
    print("73.3: ")
    test = ["A", "E", "I", "O", "U", "Y"]
    test_ascii = list(map(ord, test))
    seq = []
    for x in range(len(words)):
        word = words[x]
        tmp = []
        k = 1
        for y in range(len(word)):
            letter = word[y]
            if ord(letter) not in test_ascii:
                tmp.append(k)
                k += 1
            else:
                tmp.append(0)
                k = 1
        seq.append(max(tmp))
    i = 0
    first = 0
    for x in range(len(seq)):
        if seq[x] > i:
            i = seq[x]
            first = x

    print("first occurrence - "+str(words[first]))
    print("max length: "+str(max(seq)))
    print("how many: "+str(seq.count(max(seq))))


zad1()
zad2()
zad3()