# 457 126
file = open("data/66/trojki.txt")
numbers_1 = []
numbers_2 = []
numbers_3 = []

for a in range(0,1000):
    line = file.readline()
    tmp = line.split()
    numbers_1.append(tmp[0])
    numbers_2.append(tmp[1])
    numbers_3.append(tmp[2])


def is_prime(number):
    num = number
    if num > 1:
        for i in range(2, num // 2):
            if (num % i) == 0:
                return False
        else:
            return True


def ex66_1():
    answer = []
    for x in range(0, 1000):
        tmp = []
        check = 0
        for y in range(len(numbers_1[x])):
            tmp.append(int(numbers_1[x][y]))
        for z in range(len(numbers_2[x])):
            tmp.append(int(numbers_2[x][z]))
        for i in range(len(tmp)):
            check += tmp[i]
        if check == int(numbers_3[x]):
            answer.append(numbers_1[x]+" "+numbers_2[x]+" "+numbers_3[x])
    print(answer)


def ex66_2():
    answer = []
    for x in range(0, 1000):
        test1 = is_prime(int(numbers_1[x]))
        test2 = is_prime(int(numbers_2[x]))
        test3 = int(numbers_1[x]) * int(numbers_2[x])
        if int(test1):
            if int(test2):
                if int(test3) == int(numbers_3[x]):
                    answer.append(numbers_1[x]+" "+numbers_2[x]+" "+numbers_3[x])
    print(answer)


def ex66_3():
    answer = []
    for x in range(1, 1000):
        a = int(numbers_1[x])
        b = int(numbers_2[x])
        c = int(numbers_3[x])
        tmp = []
        tmp.append(a)
        tmp.append(b)
        tmp.append(c)
        find_biggest = tmp.index(max(tmp))
        biggest = tmp[find_biggest]
        tmp.pop(find_biggest)
        test = tmp[0]**2 + tmp[1]**2
        if test == biggest**2:
            answer.append(numbers_1[x]+" "+numbers_2[x]+" "+numbers_3[x])

    print(answer)


ex66_3()
