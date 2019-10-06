data = open("dane/65/dane_ulamki.txt")
counters = []
denominators = []

for x in range(0, 1000):
    number = data.readline()
    number = number.split()
    counters.append(int(number[0]))
    denominators.append(int(number[1]))


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    r = a % b
    if r == 0:
        return b
    return gcd(r, b)


def ex65_1():
    minimum = 10
    for y in range(0, 1000):
        counter = counters[y]
        denominator = denominators[y]
        if counter / denominator < minimum:
            minimum = counter / denominator
            answer = str(counter)+"/"+str(denominator)
    print(answer)


def ex65_2():
    how_many = 0
    for y in range(0, 1000):
        counter = counters[y]
        denominator = denominators[y]
        divisor = gcd(counter, denominator)
        if divisor == 1:
            how_many += 1
    print(how_many)


def ex65_3():
    summed_counters = 0
    for y in range(0, 1000):
        counter = counters[y]
        denominator = denominators[y]
        divisor = gcd(counter, denominator)
        counter = counter/divisor
        # denominator = denominator/divisor
        summed_counters += int(counter)
    print(summed_counters)


def ex65_4():
    counters_multiplied = []
    denominators_multiplied = []
    b = (2**2) * (3**2) * (5**2) * (7**2) * 13
    for y in range(0, 1000):
        counter = counters[y]
        denominator = denominators[y]

        rest = b / denominator
        counters_multiplied.append(counter*rest)
        denominators_multiplied.append(denominator*rest)

    print(int(sum(counters_multiplied)))




# ex65_1()
# ex65_2()
# ex65_3()
# ex65_4()
