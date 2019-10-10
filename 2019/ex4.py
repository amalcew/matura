from math import gcd

def multiply(n):
    total = 1
    for i in range(0, len(n)):
        total *= n[i]
    return total


def ex4_1():
    how_many = 0
    power = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers = open("data/liczby.txt", "r")
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
    numbers = open("data/liczby.txt", "r")
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
    data = open("data/liczby.txt", "r")
    numbers = []
    # convert file to list of ints
    for i in range(0, 500):
        numbers.append(int(data.readline()))

    series = []
    tmp_series = [numbers[0]]
    # main loop
    for x in range(1, 500):
        tmp_series.append(numbers[x])
        # check GCD for series of numbers
        check = tmp_series[0]
        for y in tmp_series[1:]:
            check = gcd(check, y)

        if check == 1:
            # delete invalid number
            tmp_series.pop()
            if len(tmp_series) > len(series):
                series.clear()
                # convert tmp_series to series
                for z in range(len(tmp_series)):
                    series.append(tmp_series[z])
            # clear temporary list
            tmp_series.clear()
            # append last number and invalid number
            tmp_series.append(numbers[x-1])
            tmp_series.append(numbers[x])
    # check GCD for the series
    max_divisor = series[0]
    for j in series[1:]:
        max_divisor = gcd(max_divisor, j)
    # answer
    print("Pierwsza  liczba: "+str(series[0]))
    print("Długość: "+str(len(series)))
    print("NWD: "+str(max_divisor))
    data.close()


ex4_1()
ex4_2()
ex4_3()
