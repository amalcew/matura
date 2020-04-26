# initialize data
file = open("data/sygnaly.txt")
file = file.readlines()
data = []
for line in file:
    data.append(line.rstrip())


def ex4_1():
    print("4.1")
    answer = []
    for x in range(len(data)):
        if (x+1) % 40 == 0:
            answer.append(data[x][9])
    print(''.join(answer))
    print()


def ex4_2():
    print("4.2")
    words = []
    lengths = []
    for x in range(len(data)):
        word = data[x]
        word_unique = set(word)
        # print(word_unique)
        words.append(str(len(word_unique))+" "+str(word))
        lengths.append(len(word_unique))
    m = max(lengths)
    for x in range(len(words)):
        s = words[x].split()
        if int(s[0]) == m:
            print(str(s[1])+" "+str(s[0]))
            break
    print()


def ex4_3():
    print("4.3")
    for x in range(len(data)):
        word = data[x]
        word_list = list(word)
        order = []
        for y in range(len(word_list)):
            order.append(ord(word_list[y]))
        if max(order) - min(order) <= 10:
            print(word)


ex4_1()
ex4_2()
ex4_3()
