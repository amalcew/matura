def ex68_1():
    file = open("data/68/dane_napisy.txt", "r")
    a_lines = []
    b_lines = []
    for x in range(0, 1000):
        line = file.readline()
        tmp = line.split()
        a_lines.append(tmp[0])
        b_lines.append((tmp[1]))

    k = 0
    for y in range(0, 1000):
        if a_lines[y] == b_lines[y]:
            k += 1
    print(k)
    file.close()


def ex68_2():
    file = open("data/68/dane_napisy.txt", "r")
    a_lines = []
    b_lines = []
    for x in range(0, 1000):
        line = file.readline()
        tmp = line.split()
        a_lines.append(tmp[0])
        b_lines.append((tmp[1]))

    k = 0
    for y in range(0, 1000):
        a_set = set(a_lines[y])
        a_unique = list(a_set)
        a_unique = sorted(a_unique)
        a_word = list(a_lines[y])
        a_count = []
        for z in range(len(a_unique)):
            how_many_in_a = a_word.count(a_unique[z])
            a_count.append(how_many_in_a)

        b_set = set(b_lines[y])
        b_unique = list(b_set)
        b_unique = sorted(b_unique)
        b_word = list(b_lines[y])
        b_count = []
        for z in range(len(b_unique)):
            how_many_in_b = b_word.count(b_unique[z])
            b_count.append(how_many_in_b)

        if a_unique == b_unique:
            if a_count == b_count:
                k += 1
    print(k)
    file.close()
