data = open('dane/62/liczby1.txt', 'r')
data2 = open('dane/62/liczby2.txt', 'r')


def oct_to_dec(octal):
    decimal, i = 0, 0
    while (octal != 0):
        dec_num = octal % 10
        decimal = decimal + dec_num * pow(8, i)
        octal = octal // 10
        i += 1
    return decimal


def dec_to_oct(decimal):
    octal, i = 0, 0
    while (decimal != 0):
        oct_num = decimal % 8
        octal = octal + oct_num * pow(10, i)
        decimal = decimal // 8
        i += 1
    return octal


def ex62_1():
    numbers = []
    for x in range(0, 1000):
        number = data.readline()
        number = int(number)
        numbers.append(number)
    print(max(numbers))
    print(min(numbers))


def ex62_3():
    equal = 0
    number8_bigger = 0
    for x in range(0, 1000):
        number8 = data.readline()
        number8 = int(number8)
        number8 = oct_to_dec(number8)
        number10 = data2.readline()
        number10 = int(number10)

        if number8 == number10:
            equal += 1
        if number8 > number10:
            number8_bigger += 1
    print("Equal values: "+str(equal))
    print("Bigger octal values: "+str(number8_bigger))


def ex62_4():
    numbers = []
    for x in range(0, 1000):
        number = data2.readline()
        number = int(number)
        numbers.append(number)

    how_many_10 = 0
    for x in range(len(numbers)):
        str_num = str(numbers[x])
        for y in range(len(str_num)):
            if str_num[y] == '6':
                how_many_10 += 1
    print('How many "6" in decimal numbers: '+str(how_many_10))

    how_many_8 = 0
    for x in range(len(numbers)):
        num = dec_to_oct(numbers[x])
        str_num = str(num)
        for y in range(len(str_num)):
            if str_num[y] == '6':
                how_many_8 += 1
    print('How many "6" in octal numbers: '+str(how_many_8))


# ex62_1()
# ex62_3()
ex62_4()
