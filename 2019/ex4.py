def test():
    flag = True
    while flag:
        for x in range(0, 5000):
            number = 3 ** x
            if number < 100000:
                print(number)
            else:
                flag = False


def multiply(n):
    total = 1
    for i in range(0, len(n)):
        total *= n[i]
    return total


def ex4_1():
    how_many = 0
    power = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = open("Dane_PR2/liczby.txt", "r")
    for x in range(0, 500):
        number = numbers.readline()
        number = int(number)
        for y in range(len(power)):
            check = 3 ** y
            if check == number:
                how_many += 1
                break
    print(how_many)
    numbers.close()


def ex4_2():
    numbers = open("Dane_PR2/liczby.txt", "r")
    for x in range(0, 500):
        number = numbers.readline()
        check = int(number)
        number = list(number)
        number.pop()
        number = list(map(int, number))
        summ = []
        for y in range(len(number)):
            power = []
            number[y] = number[y]+1
            while number[y] > 1:
                number[y] -= 1
                power.append(number[y])
            summ.append(multiply(power))
        summ = sum(summ)
        if check == summ:
            print(check)
    numbers.close()


def ex4_3():
    pass


ex4_2()
