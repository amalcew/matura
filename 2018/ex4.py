def zadanie4_1():
    wega = open("dane_matury_probne/sygnaly.txt", 'r')
    answer = open("wyniki4.txt", 'w')
    answer.write("4.1 - ")

    x = 1
    while x <= 1000:
        a = x % 40
        if a == 0:
            line = wega.readline()
            for c in line[9:10:1]:
                answer.write(c)
            x += 1
        wega.readline()
        x += 1

    wega.close()
    answer.close()


def zadanie4_2():
    wega = open("dane_matury_probne/sygnaly.txt", 'r')
    answer = open("wyniki4.txt", 'a')
    answer.write("\n4.2 - ")

    words = []
    chars = []

    for x in range(1, 1000):
        line = wega.readline()
        line = line[:-1]
        unique_chars = len(set(line))
        words.append(line + " " + str(unique_chars))
        chars.append(unique_chars)

    max_value = max(chars)
    max_index = chars.index(max_value)
    answer.write(words[max_index])

    wega.close()
    answer.close()


def zadanie4_3():
    wega = open("dane_matury_probne/sygnaly.txt", 'r')
    answer = open("wyniki4.txt", 'a')
    answer.write("\n4.3 - \n")

    ascii_chars = []
    for x in range(1, 1000):
        line = wega.readline()
        for c in line:
            ascii_chars.append(ord(c))
        ascii_chars.pop()
        # print(ascii_chars)
        if max(ascii_chars) - min(ascii_chars) <= 10:
            # print(line)
            answer.write(line)
        ascii_chars.clear()

    wega.close()
    answer.close()


if __name__ == '__main__':
    zadanie4_1()
    zadanie4_2()
    zadanie4_3()
