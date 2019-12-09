def fibonacci(number):
    sequence = []
    for x in range(0, number):
        if x == 0 or x == 1:
            num = 1
            sequence.append(num)
        else:
            num = sequence[x-1] + sequence[x-2]
            sequence.append(num)
    return sequence[-1]


def number_converter(system_before, system_after, number):
    number_after, i = 0, 0
    while number != 0:
        index = number % system_after
        number_after = number_after + index * pow(system_before, i)
        number = number // system_after
        i += 1
    return number_after


def is_prime(number):
    num = number
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def ex67_1():
    x = 10
    while x < 50:
        number = fibonacci(x)
        print(number)
        x += 10


def ex67_2():
    for x in range(1, 41):
        number = fibonacci(x)
        if is_prime(number):
            print(str(x)+" "+str(number))


def ex67_3():
    tmp = []
    fractal = []
    for x in range(1, 41):
        number = fibonacci(x)
        number_bin = number_converter(10, 2, number)
        tmp.append(str(number_bin))

    length = len(tmp[-1])
    for y in range(len(tmp)):
        bin_length = len(tmp[y])
        line = tmp[y]
        while bin_length < length:
            line = "0" + line
            bin_length += 1
        fractal.append(line)

    for z in range(len(fractal)):
        print(fractal[z])


def ex67_4():
    fractal = []
    for x in range(1, 41):
        number = fibonacci(x)
        number_bin = number_converter(10, 2, number)
        fractal.append(str(number_bin))

    for y in range(len(fractal)):
        how_many = fractal[y].count("1")
        if how_many == 6:
            print(fractal[y])


ex67_3()
