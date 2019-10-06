numbers = open("dane/59/liczby.txt", "r")


def ex59_1():
    print("exercise 59.1: \n")
    output = 0
    for x in range(1, 1001):
        number = numbers.readline()
        number = int(number)
        output_number = number

        answer = 0
        factor = 3
        if number % 2 == 0:
            pass
        else:
            while number > 1:
                if number % factor == 0:
                    answer += 1
                while number % factor == 0:
                    number = number // factor
                factor += 2
        if answer == 3:
            output += 1
            print(output)
            print("true element = " + str(output_number))


def ex59_2():
    output = 0
    for x in range(1, 1001):
        number = numbers.readline()
        number_reversed = number[::-1]
        number = int(number)
        number_reversed = int(number_reversed)

        result = number + number_reversed
        result = str(result)
        result_reversed = result[::-1]
        if str(result) == str(result_reversed):
            output += 1
    print(output)


def ex59_3():
    results = []
    min_max = []
    for x in range(1, 1001):
        output = 1
        number = numbers.readline()
        number_list = list(number)
        number_list.pop()
        number_list = list(map(int, number_list))
        while len(number_list) != 1:
            number_multiplied = 1
            for y in number_list:
                number_multiplied *= y

            number_multiplied = str(number_multiplied)
            number_list = list(map(int, number_multiplied))

            if int(number_multiplied) != 0 and len(number_list) != 1:
                output += 1
        results.append(output)

        if output == 1:
            min_max.append(number[0:-1])
            min_max = list(map(int, min_max))

    for z in range(1, 9):
        result = results.count(z)
        print("Numbers with power "+str(z)+": "+str(result))
    print("\nMinimal number with power 1: "+str(min(min_max)))
    print("Maximal number with power 1: " + str(max(min_max)))


ex59_1()
ex59_2()
ex59_3()
