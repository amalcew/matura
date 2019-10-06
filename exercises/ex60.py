numbers = open("dane/60/liczby.txt", "r")


def ex60_1():
    less_than_1000 = []
    for x in range(1, 201):
        number = numbers.readline()
        if int(number) < 1000:
            less_than_1000.append(number)

    last_numbers = str(less_than_1000[-2]) + str(less_than_1000[-1])
    print("Less than 1000: " + str(len(less_than_1000)))
    print("Two last numbers smaller than 1000: " + last_numbers)


def ex60_2():
    print("Exercise 60.2 - numbers with 18 dividors: ")
    for x in range(1, 201):
        number = numbers.readline()
        number = int(number)
        index = 1
        dividers = []
        while index <= number:
            if number % index == 0:
                dividers.append(index)
            index += 1
        if len(dividers) == 18:
            print(str(number)+" - "+str(dividers))


def ex60_3():
    numbers_with_dividers = []
    numbers_index = []
    numbers_relatively_prime = []
    for x in range(1, 201):
        number = numbers.readline()
        number = int(number)
        numbers_index.append(number)

        index = 1
        dividers = []
        while index <= number:
            if number % index == 0:
                dividers.append(index)
            index += 1
        numbers_with_dividers.append(dividers)

    for y in range(len(numbers_with_dividers)):
        for z in range(len(dividers)):
            # TODO condition doesn't work. Modifications needed
            condition = list(set(numbers_with_dividers[y]) & set(numbers_with_dividers[z]))
            if len(condition) == 1:
                numbers_relatively_prime.append(numbers_index[y])

    print(max(numbers_relatively_prime))


# ex60_1()
# ex60_2()
ex60_3()
