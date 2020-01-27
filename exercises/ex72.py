# 462
file = open("data/72/napisy.txt")
file = file.readlines()
lines = []
for x in range(len(file)):
    line = file[x].split()
    lines.append(line)


def ex1():
    print("zadanie 72.1")
    answer = []
    for x in range(len(lines)):
        line = lines[x]
        a = len(line[0])
        b = len(line[1])
        tmp = [a, b]
        ma_x = max(tmp)
        tmp.remove(max(tmp))
        mi_n = tmp[0]

        if ma_x / mi_n >= 3:
            answer.append(line)

    print(len(answer))
    print(answer[0])
    print()


def ex2():
    print("zadanie 72.2")
    for x in range(len(lines)):
        line = lines[x]
        a = line[0]
        b = line[1]
        if a in b:
            rest = b.split(a)
            if len(rest[0]) == 0:
                print(' '.join(line))
                print(rest[1])
    print()


def ex3():
    print("zadanie 72.3")
    max_length = 0
    how_many = []
    for i in range(len(lines)):
        line = lines[i]
        a = line[0]
        b = line[1]
        x = -1
        length = 0
        while True:
            if a[x] == b[x]:
                length += 1
                x -= 1
            else:
                break
        if length == max_length:
            how_many.append(line)
        if length > max_length:
            max_length = length
            how_many.clear()
            how_many.append(line)

    print(max_length)
    print(how_many)

ex1()
ex2()
ex3()